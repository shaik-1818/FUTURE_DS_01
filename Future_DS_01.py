# ============================================================
#   FUTURE INTERNS — DATA SCIENCE & ANALYTICS
#   Task 1 : Business Sales Performance Analytics
#   Repo   : FUTURE_DS_01
#   Dataset: SampleSuperstore.csv
#   Tools  : Python, Pandas, Matplotlib, Seaborn, ReportLab
# ============================================================

# ── STEP 0 : Install dependencies (run once) ────────────────
# pip install pandas matplotlib seaborn reportlab

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
import warnings
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                 Image, Table, TableStyle, HRFlowable)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY

warnings.filterwarnings('ignore')
sns.set_theme(style='whitegrid')
plt.rcParams['figure.dpi'] = 130
plt.rcParams['font.family'] = 'DejaVu Sans'

# ════════════════════════════════════════════════════════════
# SECTION 1 — LOAD & CLEAN DATA
# ════════════════════════════════════════════════════════════

print("=" * 55)
print("  FUTURE_DS_01 — Business Sales Performance Analytics")
print("=" * 55)

df = pd.read_csv('SampleSuperstore.csv')
print(f"\n✅ Dataset loaded  : {df.shape[0]} rows × {df.shape[1]} columns")

# Remove duplicates
before = len(df)
df.drop_duplicates(inplace=True)
print(f"✅ Duplicates removed : {before - len(df)} rows dropped")

# Check missing values
missing = df.isnull().sum().sum()
print(f"✅ Missing values  : {missing}")

# Feature engineering
df['Profit Margin (%)'] = (df['Profit'] / df['Sales']) * 100
df['Revenue per Unit']  = df['Sales'] / df['Quantity']

print(f"\n{'─'*55}")
print(f"  OVERALL BUSINESS SUMMARY")
print(f"{'─'*55}")
total_sales   = df['Sales'].sum()
total_profit  = df['Profit'].sum()
total_orders  = len(df)
avg_discount  = df['Discount'].mean() * 100
profit_margin = (total_profit / total_sales) * 100

print(f"  Total Revenue    : ${total_sales:>12,.2f}")
print(f"  Total Profit     : ${total_profit:>12,.2f}")
print(f"  Total Orders     : {total_orders:>13,}")
print(f"  Avg Discount     : {avg_discount:>12.1f}%")
print(f"  Profit Margin    : {profit_margin:>12.2f}%")
print(f"{'─'*55}\n")


# ════════════════════════════════════════════════════════════
# SECTION 2 — KPI DASHBOARD
# ════════════════════════════════════════════════════════════

fig, axes = plt.subplots(1, 5, figsize=(10, 3))
fig.patch.set_facecolor('#1e1e2e')

kpis = [
    ('Total Revenue',  f'${total_sales/1e6:.2f}M', '#4361ee'),
    ('Total Profit',   f'${total_profit/1e3:.1f}K', '#2dc653'),
    ('Total Orders',   f'{total_orders:,}',          '#f72585'),
    ('Avg Discount',   f'{avg_discount:.1f}%',        '#7b2d8b'),
    ('Profit Margin',  f'{profit_margin:.1f}%',       '#f8961e'),
]
for ax, (title, value, color) in zip(axes, kpis):
    ax.set_facecolor(color)
    ax.text(0.5, 0.58, value, ha='center', va='center',
            fontsize=24, fontweight='bold', color='white',
            transform=ax.transAxes)
    ax.text(0.5, 0.22, title, ha='center', va='center',
            fontsize=10, color='#ffffffcc', transform=ax.transAxes)
    ax.axis('off')

plt.suptitle('📊 Business KPI Overview — Sample Superstore',
             fontsize=14, fontweight='bold', color='white', y=1.06)
plt.tight_layout(pad=0.5)
plt.savefig('kpi.png', bbox_inches='tight', facecolor=fig.get_facecolor())
plt.show()
print("📊 Chart 1 saved  : kpi.png")


# ════════════════════════════════════════════════════════════
# SECTION 3 — CATEGORY & SUB-CATEGORY ANALYSIS
# ════════════════════════════════════════════════════════════

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# --- Grouped bar: Category Sales vs Profit ---
cat_data = df.groupby('Category')[['Sales', 'Profit']].sum()\
             .sort_values('Sales', ascending=False)
x = range(len(cat_data))
w = 0.35
b1 = axes[0].bar([i - w/2 for i in x], cat_data['Sales'],
                  width=w, label='Sales',  color='#4361ee', edgecolor='white')
b2 = axes[0].bar([i + w/2 for i in x], cat_data['Profit'],
                  width=w, label='Profit', color='#2dc653', edgecolor='white')
axes[0].set_xticks(list(x))
axes[0].set_xticklabels(cat_data.index, fontsize=11)
axes[0].yaxis.set_major_formatter(
    mtick.FuncFormatter(lambda x, _: f'${x/1e3:.0f}K'))
axes[0].set_title('Sales & Profit by Category',
                   fontweight='bold', fontsize=13)
axes[0].legend()
for i, (s, p) in enumerate(zip(cat_data['Sales'], cat_data['Profit'])):
    axes[0].text(i - w/2, s + 5000, f'${s/1e3:.0f}K',
                 ha='center', fontsize=8, color='#4361ee')
    axes[0].text(i + w/2, p + 5000, f'${p/1e3:.0f}K',
                 ha='center', fontsize=8, color='#2dc653')

# --- Horizontal bar: Top 10 Sub-Categories ---
sub_data = df.groupby('Sub-Category')['Sales'].sum()\
             .sort_values(ascending=True).tail(10)
bars = axes[1].barh(sub_data.index, sub_data.values,
                    color='#4361ee', edgecolor='white')
axes[1].xaxis.set_major_formatter(
    mtick.FuncFormatter(lambda x, _: f'${x/1e3:.0f}K'))
axes[1].set_title('Top 10 Sub-Categories by Sales',
                   fontweight='bold', fontsize=13)
for bar, val in zip(bars, sub_data.values):
    axes[1].text(val + 1000, bar.get_y() + bar.get_height() / 2,
                 f'${val/1e3:.1f}K', va='center', fontsize=8)

plt.tight_layout()
plt.savefig('category_chart.png', bbox_inches='tight')
plt.show()
print("📊 Chart 2 saved  : category_chart.png")


# ════════════════════════════════════════════════════════════
# SECTION 4 — REGIONAL PERFORMANCE
# ════════════════════════════════════════════════════════════

region_data = df.groupby('Region').agg(
    Sales=('Sales',  'sum'),
    Profit=('Profit', 'sum'),
    Orders=('Sales',  'count')
).reset_index()
region_data['Margin (%)'] = (
    region_data['Profit'] / region_data['Sales'] * 100).round(2)

print("\n📍 Regional Summary:")
print(region_data.to_string(index=False))

fig, axes = plt.subplots(1, 3, figsize=(10, 4))
palette = ['#4361ee', '#f72585', '#2dc653', '#f8961e']

for i, (col, title, fmt) in enumerate([
    ('Sales',       'Total Sales by Region',      'dollar'),
    ('Profit',      'Total Profit by Region',      'dollar'),
    ('Margin (%)',  'Profit Margin % by Region',   'pct'),
]):
    bars = axes[i].bar(region_data['Region'], region_data[col],
                       color=palette, edgecolor='white', linewidth=0.8)
    axes[i].set_title(title, fontweight='bold', fontsize=12)
    if fmt == 'dollar':
        axes[i].yaxis.set_major_formatter(
            mtick.FuncFormatter(lambda x, _: f'${x/1e3:.0f}K'))
    else:
        axes[i].yaxis.set_major_formatter(mtick.PercentFormatter())
    for bar, val in zip(bars, region_data[col]):
        label = f'${val/1e3:.1f}K' if fmt == 'dollar' else f'{val:.1f}%'
        axes[i].text(bar.get_x() + bar.get_width() / 2,
                     bar.get_height() + max(region_data[col]) * 0.015,
                     label, ha='center', fontsize=9, fontweight='bold')

plt.suptitle('Regional Performance Breakdown',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('regional_chart.png', bbox_inches='tight')
plt.show()
print("📊 Chart 3 saved  : regional_chart.png")


# ════════════════════════════════════════════════════════════
# SECTION 5 — DISCOUNT vs PROFIT ANALYSIS
# ════════════════════════════════════════════════════════════

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# --- Scatter: Discount vs Profit ---
colors_cat = {
    'Furniture':       '#f72585',
    'Office Supplies': '#4361ee',
    'Technology':      '#2dc653'
}
for cat, grp in df.groupby('Category'):
    axes[0].scatter(grp['Discount'], grp['Profit'],
                    alpha=0.35, label=cat,
                    color=colors_cat[cat], s=18)
axes[0].axhline(0, color='red', linestyle='--',
                linewidth=1.2, label='Break-even')
axes[0].set_xlabel('Discount Rate', fontsize=11)
axes[0].set_ylabel('Profit ($)',    fontsize=11)
axes[0].set_title('Discount vs Profit (by Category)',
                   fontweight='bold', fontsize=13)
axes[0].legend(fontsize=9)

corr = df['Discount'].corr(df['Profit'])
axes[0].text(0.04, 0.92,
             f'Pearson r = {corr:.3f}',
             transform=axes[0].transAxes, fontsize=10,
             bbox=dict(facecolor='#fff9c4', edgecolor='gray', alpha=0.9))

print(f"\n📉 Discount–Profit Correlation : {corr:.3f}")

# --- Horizontal bar: Sub-Category Profit (all, red = loss) ---
sub_profit  = df.groupby('Sub-Category')['Profit'].sum().sort_values()
bar_colors  = ['#f72585' if v < 0 else '#2dc653' for v in sub_profit]
axes[1].barh(sub_profit.index, sub_profit.values,
             color=bar_colors, edgecolor='white')
axes[1].axvline(0, color='black', linewidth=1)
axes[1].xaxis.set_major_formatter(
    mtick.FuncFormatter(lambda x, _: f'${x/1e3:.0f}K'))
axes[1].set_title('Profit by Sub-Category  🔴=Loss  🟢=Profit',
                   fontweight='bold', fontsize=12)
for val, y_pos in zip(sub_profit.values,
                      range(len(sub_profit))):
    axes[1].text(val + (1500 if val >= 0 else -1500), y_pos,
                 f'${val/1e3:.1f}K', va='center',
                 ha='left' if val >= 0 else 'right', fontsize=7.5)

loss_list = sub_profit[sub_profit < 0].index.tolist()
print(f"🔴 Loss-making sub-categories : {loss_list}")

plt.tight_layout()
plt.savefig('discount_profit.png', bbox_inches='tight')
plt.show()
print("📊 Chart 4 saved  : discount_profit.png")


# ════════════════════════════════════════════════════════════
# SECTION 6 — CUSTOMER SEGMENT ANALYSIS
# ════════════════════════════════════════════════════════════

seg_data = df.groupby('Segment').agg(
    Sales=('Sales',  'sum'),
    Profit=('Profit', 'sum'),
    Orders=('Sales',  'count')
).reset_index()
seg_data['Margin (%)'] = (
    seg_data['Profit'] / seg_data['Sales'] * 100).round(2)

print("\n👥 Segment Summary:")
print(seg_data.to_string(index=False))

fig, axes = plt.subplots(1, 3, figsize=(10, 4))
palette   = ['#4361ee', '#f72585', '#2dc653']
explode   = (0.04, 0.04, 0.04)

axes[0].pie(seg_data['Sales'], labels=seg_data['Segment'],
            autopct='%1.1f%%', colors=palette,
            startangle=90, explode=explode,
            wedgeprops=dict(edgecolor='white', linewidth=1.5))
axes[0].set_title('Sales Share by Segment',
                   fontweight='bold', fontsize=12)

axes[1].pie(seg_data['Profit'], labels=seg_data['Segment'],
            autopct='%1.1f%%', colors=palette,
            startangle=90, explode=explode,
            wedgeprops=dict(edgecolor='white', linewidth=1.5))
axes[1].set_title('Profit Share by Segment',
                   fontweight='bold', fontsize=12)

# Top 10 states by profit
top_states  = df.groupby('State')['Profit'].sum().nlargest(10)\
               .sort_values()
bar_colors2 = ['#f72585' if v < 0 else '#4361ee' for v in top_states]
top_states.plot(kind='barh', ax=axes[2],
                color=bar_colors2, edgecolor='white')
axes[2].xaxis.set_major_formatter(
    mtick.FuncFormatter(lambda x, _: f'${x/1e3:.0f}K'))
axes[2].set_title('Top 10 States by Profit',
                   fontweight='bold', fontsize=12)
axes[2].axvline(0, color='black', linewidth=0.8)

plt.tight_layout()
plt.savefig('segment_states.png', bbox_inches='tight')
plt.show()
print("📊 Chart 5 saved  : segment_states.png")


# ════════════════════════════════════════════════════════════
# SECTION 7 — SHIP MODE & HEATMAP
# ════════════════════════════════════════════════════════════

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# --- Ship Mode grouped bar ---
ship = df.groupby('Ship Mode')[['Sales', 'Profit']].sum()\
         .sort_values('Sales', ascending=False)
x = range(len(ship))
w = 0.35
axes[0].bar([i - w/2 for i in x], ship['Sales'],
            width=w, label='Sales',  color='#4361ee', edgecolor='white')
axes[0].bar([i + w/2 for i in x], ship['Profit'],
            width=w, label='Profit', color='#2dc653', edgecolor='white')
axes[0].set_xticks(list(x))
axes[0].set_xticklabels(ship.index, fontsize=10)
axes[0].yaxis.set_major_formatter(
    mtick.FuncFormatter(lambda x, _: f'${x/1e3:.0f}K'))
axes[0].set_title('Sales & Profit by Ship Mode',
                   fontweight='bold', fontsize=13)
axes[0].legend()

# --- Heatmap: Region × Category Profit ---
pivot = df.pivot_table(values='Profit', index='Region',
                       columns='Category', aggfunc='sum')
sns.heatmap(pivot, ax=axes[1], annot=True, fmt='.0f',
            cmap='RdYlGn', linewidths=0.5, linecolor='white',
            annot_kws={'size': 11, 'weight': 'bold'})
axes[1].set_title('Profit Heatmap: Region × Category',
                   fontweight='bold', fontsize=13)
axes[1].set_xlabel('')
axes[1].set_ylabel('')

plt.tight_layout()
plt.savefig('shipmode_heatmap.png', bbox_inches='tight')
plt.show()
print("📊 Chart 6 saved  : shipmode_heatmap.png")


# ════════════════════════════════════════════════════════════
# SECTION 8 — KEY INSIGHTS (printed)
# ════════════════════════════════════════════════════════════

top_cat    = df.groupby('Category')['Sales'].sum().idxmax()
top_sub    = df.groupby('Sub-Category')['Sales'].sum().idxmax()
top_region = df.groupby('Region')['Sales'].sum().idxmax()
top_seg    = df.groupby('Segment')['Profit'].sum().idxmax()

print(f"""
╔══════════════════════════════════════════════════════════╗
║         KEY BUSINESS INSIGHTS — SAMPLE SUPERSTORE       ║
╠══════════════════════════════════════════════════════════╣
║  1. Top Revenue Category    : {top_cat:<27}║
║  2. Top Revenue Sub-Category: {top_sub:<27}║
║  3. Highest Sales Region    : {top_region:<27}║
║  4. Most Profitable Segment : {top_seg:<27}║
║  5. Loss-making Sub-Cats    : {str(loss_list):<27}║
║  6. Discount-Profit Corr.   : {str(round(corr,3)):<27}║
╠══════════════════════════════════════════════════════════╣
║                  RECOMMENDATIONS                        ║
╠══════════════════════════════════════════════════════════╣
║  ✅ Cap discounts at 20% across all categories           ║
║  ✅ Focus budget on West & East regions (highest ROI)    ║
║  ✅ Upsell Technology products to Corporate clients      ║
║  ⚠️  Fix pricing on Tables, Bookcases, Supplies          ║
║  ⚠️  Central region needs stricter discount controls     ║
╚══════════════════════════════════════════════════════════╝
""")


# ════════════════════════════════════════════════════════════
# SECTION 9 — GENERATE PDF REPORT
# ════════════════════════════════════════════════════════════

doc    = SimpleDocTemplate(
    'FUTURE_DS_01_Report.pdf', pagesize=A4,
    rightMargin=1.8*cm, leftMargin=1.8*cm,
    topMargin=1.5*cm,   bottomMargin=1.5*cm)
styles = getSampleStyleSheet()
story  = []

# ── Paragraph styles ──────────────────────────────────────
title_style = ParagraphStyle(
    'MyTitle', parent=styles['Title'],
    fontSize=20, textColor=colors.HexColor('#1a1a2e'),
    spaceAfter=4, alignment=TA_CENTER, fontName='Helvetica-Bold')
sub_style = ParagraphStyle(
    'MySub', parent=styles['Normal'],
    fontSize=10, textColor=colors.HexColor('#555555'),
    alignment=TA_CENTER, spaceAfter=12)
h2_style = ParagraphStyle(
    'MyH2', parent=styles['Heading2'],
    fontSize=13, textColor=colors.HexColor('#4361ee'),
    spaceBefore=14, spaceAfter=6, fontName='Helvetica-Bold')
insight_style = ParagraphStyle(
    'Insight', parent=styles['Normal'],
    fontSize=9.5, leading=15,
    textColor=colors.HexColor('#1a1a2e'), leftIndent=10)
cap_style = ParagraphStyle(
    'Cap', parent=styles['Normal'],
    fontSize=8.5, textColor=colors.HexColor('#888888'),
    alignment=TA_CENTER, spaceAfter=6)

# ── Cover ─────────────────────────────────────────────────
story.append(Spacer(1, 0.5*cm))
story.append(Paragraph('Business Sales Performance Analytics', title_style))
story.append(Paragraph(
    'Future Interns — Data Science &amp; Analytics | Task 1 (FUTURE_DS_01)',
    sub_style))
story.append(Paragraph(
    'Dataset: Sample Superstore &nbsp;|&nbsp; Tools: Python, Pandas, Matplotlib, Seaborn',
    sub_style))
story.append(HRFlowable(width='100%', thickness=2,
                        color=colors.HexColor('#4361ee'), spaceAfter=10))

# ── KPI Summary Table ─────────────────────────────────────
story.append(Paragraph('Executive KPI Summary', h2_style))
kpi_data = [
    ['Metric', 'Value', 'Metric', 'Value'],
    ['Total Revenue',  f'${total_sales:,.0f}',  'Total Profit',  f'${total_profit:,.0f}'],
    ['Total Orders',   f'{total_orders:,}',      'Avg Discount',  f'{avg_discount:.1f}%'],
    ['Profit Margin',  f'{profit_margin:.2f}%',  'Top Category',  top_cat],
    ['Top Region',     top_region,               'Top Segment',   top_seg],
]
kpi_table = Table(kpi_data,
                  colWidths=[4.5*cm, 4.2*cm, 4.5*cm, 4.2*cm])
kpi_table.setStyle(TableStyle([
    ('BACKGROUND',   (0, 0), (-1, 0),  colors.HexColor('#4361ee')),
    ('TEXTCOLOR',    (0, 0), (-1, 0),  colors.white),
    ('FONTNAME',     (0, 0), (-1, 0),  'Helvetica-Bold'),
    ('FONTSIZE',     (0, 0), (-1, 0),  10),
    ('ALIGN',        (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME',     (0, 1), (0, -1),  'Helvetica-Bold'),
    ('FONTNAME',     (2, 1), (2, -1),  'Helvetica-Bold'),
    ('ROWBACKGROUNDS',(0,1), (-1, -1), [colors.HexColor('#f0f4ff'),
                                        colors.white]),
    ('GRID',         (0, 0), (-1, -1), 0.5,
                                        colors.HexColor('#cccccc')),
    ('ROWHEIGHT',    (0, 0), (-1, -1), 18),
    ('TOPPADDING',   (0, 0), (-1, -1), 4),
]))
story.append(kpi_table)
story.append(Spacer(1, 0.3*cm))

# ── Charts ────────────────────────────────────────────────
charts = [
    ('kpi.png',              'Fig 1 — KPI Dashboard',
     17*cm, 3.0*cm),
    ('category_chart.png',   'Fig 2 — Category & Sub-Category Analysis',
     17*cm, 6.0*cm),
    ('regional_chart.png',   'Fig 3 — Regional Performance Breakdown',
     17*cm, 6.0*cm),
    ('discount_profit.png',  'Fig 4 — Discount vs Profit Analysis',
     17*cm, 6.0*cm),
    ('segment_states.png',   'Fig 5 — Segment & Top States Analysis',
     17*cm, 6.0*cm),
    ('shipmode_heatmap.png', 'Fig 6 — Ship Mode & Region×Category Heatmap',
     17*cm, 6.0*cm),
]
for fname, caption, w, h in charts:
    story.append(Paragraph(caption, cap_style))
    story.append(Image(fname, width=w, height=h))
    story.append(Spacer(1, 0.2*cm))

# ── Key Insights ──────────────────────────────────────────
story.append(HRFlowable(width='100%', thickness=1.5,
                        color=colors.HexColor('#4361ee'), spaceAfter=8))
story.append(Paragraph('Key Insights', h2_style))

insights = [
    ('📈 Revenue Leader',
     f'{top_cat} is the top revenue and profit-generating category. '
     f'Office Supplies follows in volume but with thinner margins.'),
    ('🌍 Regional Champion',
     f'The {top_region} region leads in both sales and profit. '
     f'The Central region underperforms despite decent order volume.'),
    ('⚠️ Discount Impact',
     f'Discount rate has a negative correlation with profit '
     f'(r = {corr:.3f}). Orders above 40% discount almost always '
     f'result in losses.'),
    ('🔴 Loss-Making Products',
     f'Sub-categories running at a loss: {", ".join(loss_list)}. '
     f'These require an urgent pricing review.'),
    ('👥 Best Segment',
     f'Consumer segment generates the most revenue, but '
     f'{top_seg} shows the strongest profit per order — ideal for '
     f'targeted upselling.'),
    ('🚚 Shipping Efficiency',
     f'Standard Class is the most used mode and generates the highest '
     f'revenue. Same Day shipping has the lowest volume.'),
]
for title, text in insights:
    story.append(Paragraph(f'<b>{title}:</b> {text}', insight_style))
    story.append(Spacer(1, 0.15*cm))

# ── Recommendations ───────────────────────────────────────
story.append(Paragraph('Actionable Recommendations', h2_style))
recs = [
    ('Cap Discounts at 20%',
     'Implement a discount ceiling across all categories. '
     'Discounts above 40% consistently erode profitability.'),
    ('Review Loss-Making SKUs',
     f'Conduct a pricing audit on {", ".join(loss_list)}. '
     f'Consider bundling or discontinuing low-margin items.'),
    ('Invest in West & East Regions',
     'These two regions deliver the highest ROI. Allocate more '
     'marketing budget and inventory here.'),
    ('Upsell Technology to Corporate Clients',
     'Technology + Corporate is the highest-margin combination. '
     'Build targeted B2B campaigns around this segment.'),
    ('Fix Central Region Performance',
     'Central has high order counts but low margins — likely due to '
     'excessive discounting. Apply stricter discount controls here.'),
]
for i, (title, text) in enumerate(recs, 1):
    story.append(Paragraph(f'<b>{i}. {title}:</b> {text}', insight_style))
    story.append(Spacer(1, 0.12*cm))

# ── Footer ────────────────────────────────────────────────
story.append(Spacer(1, 0.4*cm))
story.append(HRFlowable(width='100%', thickness=1,
                        color=colors.HexColor('#cccccc')))
story.append(Paragraph(
    'Analysis by: [Your Name] &nbsp;|&nbsp; Future Interns — '
    'Data Science &amp; Analytics &nbsp;|&nbsp; FUTURE_DS_01',
    ParagraphStyle('foot', parent=styles['Normal'], fontSize=8,
                   textColor=colors.HexColor('#999999'),
                   alignment=TA_CENTER, spaceBefore=8)))

doc.build(story)
