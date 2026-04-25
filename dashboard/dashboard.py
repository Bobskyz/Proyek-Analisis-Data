import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

# Konfigurasi halaman
st.set_page_config(page_title="E-Commerce Analytics Dashboard", layout="wide")

# Load data dengan caching
@st.cache_data
def load_data():
    import os
    # Tentukan path folder yang sama dengan dashboard.py
    data_path = os.path.dirname(__file__)
    
    orders = pd.read_csv(os.path.join(data_path, "orders_dataset.csv"))
    order_payments = pd.read_csv(os.path.join(data_path, "order_payments_dataset.csv"))
    order_items = pd.read_csv(os.path.join(data_path, "order_items_dataset.csv"))
    products = pd.read_csv(os.path.join(data_path, "products_dataset.csv"))
    order_reviews = pd.read_csv(os.path.join(data_path, "order_reviews_dataset.csv"))
    category_translation = pd.read_csv(os.path.join(data_path, "product_category_name_translation.csv"))

    # Konversi tanggal
    date_cols = ['order_purchase_timestamp', 'order_approved_at',
                 'order_delivered_carrier_date', 'order_delivered_customer_date',
                 'order_estimated_delivery_date']
    for col in date_cols:
        orders[col] = pd.to_datetime(orders[col])

    order_reviews['review_creation_date'] = pd.to_datetime(order_reviews['review_creation_date'])
    order_items['shipping_limit_date'] = pd.to_datetime(order_items['shipping_limit_date'])

    # Filter delivered (semua tahun)
    orders_delivered = orders[orders['order_status'] == 'delivered'].copy()

    # Gabung data pendapatan
    payments_sum = order_payments.groupby('order_id')['payment_value'].sum().reset_index()
    orders_revenue = orders_delivered.merge(payments_sum, on='order_id', how='inner')
    orders_revenue['order_month'] = orders_revenue['order_purchase_timestamp'].dt.to_period('M')

    # Gabung data ulasan per kategori
    products = products.merge(category_translation, on='product_category_name', how='left')
    products['product_category_name_english'] = products['product_category_name_english'].fillna('unknown')

    items_products = order_items.merge(products[['product_id', 'product_category_name_english']], on='product_id', how='left')
    orders_products = orders_delivered[['order_id']].merge(items_products, on='order_id', how='inner')
    reviews = order_reviews[['order_id', 'review_score']].dropna()
    orders_products_reviews = orders_products.merge(reviews, on='order_id', how='inner')

    category_stats = orders_products_reviews.groupby('product_category_name_english').agg(
        avg_review_score=('review_score', 'mean'),
        total_orders=('order_id', 'nunique')
    ).reset_index()

    return orders_revenue, category_stats

# Load data
orders_revenue, category_stats = load_data()

# Sidebar filter tahun (2016, 2017, 2018)
st.sidebar.header("Filter Data")
available_years = sorted(orders_revenue['order_purchase_timestamp'].dt.year.unique())
selected_years = st.sidebar.multiselect(
    "Pilih Tahun",
    options=available_years,
    default=available_years  # default semua tahun
)

# Filter data berdasarkan tahun yang dipilih
filtered_revenue = orders_revenue[orders_revenue['order_purchase_timestamp'].dt.year.isin(selected_years)]

# Agregasi bulanan setelah filter
monthly_revenue = filtered_revenue.groupby(filtered_revenue['order_purchase_timestamp'].dt.to_period('M'))['payment_value'].sum().reset_index()
monthly_revenue['order_month'] = monthly_revenue['order_purchase_timestamp'].astype(str)

# Dashboard utama
st.title("📊 E-Commerce Public Dataset Dashboard")
st.markdown("Analisis pendapatan dan ulasan produk dari data e-commerce Brazil (2016-2018).")

# Metrik utama
col1, col2, col3 = st.columns(3)
with col1:
    total_revenue = filtered_revenue['payment_value'].sum()
    st.metric("Total Pendapatan", f"R$ {total_revenue:,.2f}")
with col2:
    avg_monthly = monthly_revenue['payment_value'].mean()
    st.metric("Rata-rata Pendapatan Bulanan", f"R$ {avg_monthly:,.2f}")
with col3:
    total_orders = filtered_revenue['order_id'].nunique()
    st.metric("Total Pesanan (Delivered)", f"{total_orders:,}")

# Visualisasi 1: Tren Pendapatan Bulanan
st.subheader("📈 Tren Pendapatan Bulanan (2016-2018)")
fig1, ax1 = plt.subplots(figsize=(12, 5))
sns.lineplot(data=monthly_revenue, x='order_month', y='payment_value', marker='o', linewidth=2, ax=ax1)
ax1.set_title('Total Pendapatan Bulanan (Hanya Pesanan Delivered)')
ax1.set_xlabel('Bulan')
ax1.set_ylabel('Pendapatan (R$)')
ax1.tick_params(axis='x', rotation=45)
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'R$ {x:,.0f}'))
st.pyplot(fig1)

# Visualisasi 2: Rata‑rata Skor Ulasan per Kategori
st.subheader("⭐ Rata-rata Skor Ulasan per Kategori Produk")
# Pilih tampilan: Top/Bottom atau Semua
view_option = st.radio("Tampilkan:", ["Top 10 & Bottom 10", "Semua Kategori"], horizontal=True)
if view_option == "Top 10 & Bottom 10":
    top_cat = category_stats.nlargest(10, 'avg_review_score')
    bottom_cat = category_stats.nsmallest(10, 'avg_review_score')
    plot_data = pd.concat([top_cat, bottom_cat]).drop_duplicates()
else:
    plot_data = category_stats

plot_data = plot_data.sort_values('avg_review_score', ascending=False)

fig2, ax2 = plt.subplots(figsize=(12, max(6, len(plot_data)*0.3)))
if view_option == "Top 10 & Bottom 10":
    colors = ['green' if x in top_cat['product_category_name_english'].values else 'red' 
              for x in plot_data['product_category_name_english']]
else:
    # Buat daftar warna sebanyak jumlah bar di plot
    colors = ['steelblue'] * len(plot_data)

sns.barplot(data=plot_data, y='product_category_name_english', x='avg_review_score', palette=colors, ax=ax2)
ax2.set_title('Rata-rata Review Score per Kategori Produk')
ax2.set_xlabel('Rata-rata Review Score')
ax2.set_ylabel('Kategori')
ax2.set_xlim(1, 5)
ax2.grid(axis='x', linestyle='--', alpha=0.5)
st.pyplot(fig2)

# Tampilkan data tabel
st.subheader("📋 Data Detail Kategori")
st.dataframe(category_stats.sort_values('avg_review_score', ascending=False).style.format({"avg_review_score": "{:.2f}"}))

# Footer
st.markdown("---")
st.caption("Dikembangkan oleh Dafin Surya | Dashboard dibuat dengan Streamlit • Sumber: E-Commerce Public Dataset (Brazilian E-Commerce) by Olist")