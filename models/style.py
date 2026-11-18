"""
style.py  —  Pink boutique styling for the clothing store app.

Usage (in app.py):
    from style import apply_theme, hero, product_card

    st.set_page_config(page_title="My Store", page_icon="👗", layout="wide")
    apply_theme()

    tab1, tab2, tab3, tab4, tab5 = st.tabs([...])   # each tab gets its own colour mood

Each of the 5 tabs changes the whole page's mood when selected:
    Tab 1  Blush    – soft and airy
    Tab 2  Rose     – warm pink
    Tab 3  Coral    – bright and lively
    Tab 4  Crimson  – bold and rich
    Tab 5  Wine     – dark, elegant mode
"""

import streamlit as st

PALETTE = {
    "blush": "#fce5e5",
    "rose": "#f7c2c2",
    "coral": "#ff7474",
    "crimson": "#c64242",
    "wine": "#541616",
}

# One colour mood per tab: page background, accent, second accent, text, card, hero gradient
TAB_MOODS = [
    # 1 Blush
    dict(bg="linear-gradient(180deg,#fffafa 0%,#fce5e5 100%)", accent="#ff7474", accent2="#c64242",
         text="#541616", muted="#8a4a4a", card="#ffffff", line="#f7c2c2",
         hero="linear-gradient(120deg,#fce5e5 0%,#f7c2c2 100%)", hero_text="#541616"),
    # 2 Rose
    dict(bg="linear-gradient(180deg,#fce5e5 0%,#f7c2c2 100%)", accent="#c64242", accent2="#ff7474",
         text="#541616", muted="#7a3a3a", card="#fffafa", line="#eeaaaa",
         hero="linear-gradient(120deg,#f7c2c2 0%,#ff7474 100%)", hero_text="#541616"),
    # 3 Coral
    dict(bg="linear-gradient(160deg,#fff4f4 0%,#ffd9d9 100%)", accent="#ff7474", accent2="#c64242",
         text="#541616", muted="#8a4a4a", card="#ffffff", line="#ffb3b3",
         hero="linear-gradient(120deg,#ff7474 0%,#c64242 100%)", hero_text="#ffffff"),
    # 4 Crimson
    dict(bg="linear-gradient(180deg,#fffafa 0%,#f7c2c2 100%)", accent="#c64242", accent2="#541616",
         text="#541616", muted="#7a3a3a", card="#ffffff", line="#e8a0a0",
         hero="linear-gradient(120deg,#c64242 0%,#541616 100%)", hero_text="#fce5e5"),
    # 5 Wine (dark mode)
    dict(bg="linear-gradient(180deg,#541616 0%,#2e0b0b 100%)", accent="#ff7474", accent2="#f7c2c2",
         text="#fce5e5", muted="#f7c2c2", card="#6b2424", line="#7a2e2e",
         hero="linear-gradient(120deg,#ff7474 0%,#c64242 100%)", hero_text="#ffffff"),
]


def _mood_vars(m: dict) -> str:
    return (
        f"--bg:{m['bg']};--accent:{m['accent']};--accent2:{m['accent2']};"
        f"--text:{m['text']};--muted:{m['muted']};--card:{m['card']};--line:{m['line']};"
        f"--hero:{m['hero']};--hero-text:{m['hero_text']};"
    )


def apply_theme() -> None:
    """Inject the boutique CSS. Call once, right after st.set_page_config()."""
    # Default mood = tab 1; each selected tab swaps the variables on the whole app.
    per_tab = "\n".join(
        f'.stApp:has(.stTabs [role="tab"]:nth-child({i + 1})[aria-selected="true"])'
        f"{{{_mood_vars(m)}}}"
        for i, m in enumerate(TAB_MOODS)
    )
    # Each tab label is tinted with its own colour, even when not selected
    tab_label_colors = "\n".join(
        f'.stTabs [role="tab"]:nth-child({i + 1})::before{{background:{m["accent"] if i != 4 else "#541616"};}}'
        for i, m in enumerate(TAB_MOODS)
    )

    st.markdown(
        f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;700&family=Poppins:wght@300;400;500;600&display=swap');

.stApp {{ {_mood_vars(TAB_MOODS[0])} }}
{per_tab}

/* ---------- Page ---------- */
.stApp {{
    background: var(--bg);
    background-attachment: fixed;
    transition: background .5s ease;
}}
.stApp, .stApp p, .stApp li, .stApp label, .stApp span,
.stApp [data-testid="stMarkdownContainer"],
.stApp [data-testid="stWidgetLabel"] p {{
    font-family: 'Poppins', sans-serif;
    color: var(--text);
}}
.stApp h1, .stApp h2, .stApp h3, .stApp h4 {{
    font-family: 'Playfair Display', serif !important;
    color: var(--text) !important;
    letter-spacing: .3px;
}}
.stApp [data-testid="stCaptionContainer"], .stApp small {{ color: var(--muted) !important; }}
header[data-testid="stHeader"] {{ background: transparent; }}
.block-container {{ padding-top: 2rem; max-width: 1200px; }}

/* ---------- Tabs: pill navigation ---------- */
.stTabs [role="tablist"] {{
    gap: .5rem;
    background: rgba(255,255,255,.55);
    backdrop-filter: blur(8px);
    padding: .45rem;
    border-radius: 999px;
    border: 1px solid var(--line);
    box-shadow: 0 6px 20px rgba(84,22,22,.08);
    justify-content: center;
    flex-wrap: wrap;
}}
.stTabs [data-baseweb="tab-highlight"],
.stTabs [data-baseweb="tab-border"],
.stTabs .react-aria-SelectionIndicator {{ display: none !important; }}
.stTabs [role="tab"] {{
    height: auto;
    padding: .55rem 1.3rem;
    border-radius: 999px;
    background: transparent;
    border: none;
    transition: all .25s ease;
    gap: .5rem;
    display: flex; align-items: center; cursor: pointer;
}}
.stTabs [role="tab"]::before {{
    content: "";
    width: 10px; height: 10px;
    border-radius: 50%;
    display: inline-block;
    margin-right: .45rem;
    box-shadow: 0 0 0 2px rgba(255,255,255,.8);
}}
{tab_label_colors}
.stTabs [role="tab"] p {{
    font-family: 'Poppins', sans-serif;
    font-weight: 500;
    font-size: .95rem;
    color: #541616 !important;
}}
.stTabs [role="tab"]:hover {{ background: rgba(247,194,194,.55); transform: translateY(-1px); }}
.stTabs [role="tab"][aria-selected="true"] {{
    background: var(--accent);
    box-shadow: 0 6px 16px rgba(198,66,66,.35);
}}
.stTabs [role="tab"][aria-selected="true"] p {{ color: #ffffff !important; }}
.stTabs [role="tab"][aria-selected="true"]::before {{ background: #ffffff !important; }}
.stTabs [role="tabpanel"] {{ padding-top: 1.5rem; animation: fadeUp .45s ease; }}
@keyframes fadeUp {{ from {{ opacity: 0; transform: translateY(10px); }} to {{ opacity: 1; transform: none; }} }}

/* ---------- Buttons ---------- */
.stButton > button, .stDownloadButton > button, .stFormSubmitButton > button {{
    background: var(--accent);
    color: #ffffff;
    border: none;
    border-radius: 999px;
    padding: .55rem 1.4rem;
    font-family: 'Poppins', sans-serif;
    font-weight: 500;
    box-shadow: 0 4px 12px rgba(198,66,66,.25);
    transition: all .2s ease;
}}
.stButton > button p, .stDownloadButton > button p, .stFormSubmitButton > button p {{ color: #ffffff !important; }}
.stButton > button:hover, .stDownloadButton > button:hover, .stFormSubmitButton > button:hover {{
    background: var(--accent2);
    color: #ffffff;
    transform: translateY(-2px);
    box-shadow: 0 8px 18px rgba(84,22,22,.3);
}}
.stButton > button:focus:not(:active) {{ color: #ffffff; border: none; }}

/* ---------- Inputs ---------- */
.stTextInput input, .stNumberInput input, .stTextArea textarea,
[data-baseweb="select"] > div {{
    border-radius: 12px !important;
    background: #ffffff !important;
    color: #541616 !important;
}}

/* ---------- Containers, metrics, expanders, forms ---------- */
[data-testid="stVerticalBlockBorderWrapper"]:has(> div > [data-testid="stVerticalBlock"]) {{
    border-radius: 18px;
}}
[data-testid="stMetric"], [data-testid="stExpander"], [data-testid="stForm"] {{
    background: var(--card);
    border: 1px solid var(--line);
    border-radius: 18px;
    padding: 1rem 1.2rem;
    box-shadow: 0 6px 18px rgba(84,22,22,.07);
}}
[data-testid="stMetricValue"] {{ font-family: 'Playfair Display', serif; color: var(--accent2); }}
[data-testid="stImage"] img {{ border-radius: 14px; }}
[data-testid="stDataFrame"] {{ border-radius: 14px; overflow: hidden; border: 1px solid var(--line); }}
hr {{ border-color: var(--line) !important; }}

/* ---------- Sidebar ---------- */
[data-testid="stSidebar"] {{
    background: linear-gradient(180deg,#541616 0%,#3a0f0f 100%);
}}
[data-testid="stSidebar"] *, [data-testid="stSidebar"] p, [data-testid="stSidebar"] label,
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {{
    color: #fce5e5 !important;
}}

/* ---------- Custom components ---------- */
.hero {{
    background: var(--hero);
    color: var(--hero-text);
    border-radius: 24px;
    padding: 2.4rem 2.6rem;
    margin-bottom: 1.6rem;
    box-shadow: 0 14px 34px rgba(84,22,22,.18);
    position: relative;
    overflow: hidden;
}}
.hero::after {{
    content: "";
    position: absolute; right: -60px; top: -60px;
    width: 220px; height: 220px; border-radius: 50%;
    background: rgba(255,255,255,.18);
}}
.hero h1 {{ color: var(--hero-text) !important; margin: 0 0 .4rem 0; font-size: 2.4rem; }}
.hero p  {{ color: var(--hero-text) !important; opacity: .9; margin: 0; font-size: 1.05rem; }}

.pcard {{
    background: var(--card);
    border: 1px solid var(--line);
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 6px 18px rgba(84,22,22,.08);
    transition: transform .25s ease, box-shadow .25s ease;
    margin-bottom: 1rem;
}}
.pcard:hover {{ transform: translateY(-5px); box-shadow: 0 14px 30px rgba(84,22,22,.16); }}
.pcard img {{ width: 100%; height: 240px; object-fit: cover; display: block; }}
.pcard .ph {{ height: 240px; display: flex; align-items: center; justify-content: center;
             font-size: 4rem; background: linear-gradient(135deg,#fce5e5,#f7c2c2); }}
.pcard .body {{ padding: .9rem 1.1rem 1.1rem; }}
.pcard .name {{ font-family: 'Playfair Display', serif; font-size: 1.1rem; color: var(--text); margin: 0; }}
.pcard .cat  {{ font-size: .8rem; color: var(--muted); text-transform: uppercase; letter-spacing: 1px; }}
.pcard .row  {{ display: flex; justify-content: space-between; align-items: center; margin-top: .5rem; }}
.pcard .price {{ font-weight: 600; color: var(--accent2); font-size: 1.1rem; }}
.pcard .tag {{ background: var(--accent); color: #fff; font-size: .72rem; padding: .2rem .65rem; border-radius: 999px; }}
</style>
""",
        unsafe_allow_html=True,
    )


def hero(title: str, subtitle: str = "") -> None:
    """Big gradient banner at the top of a tab. Its colours follow the selected tab."""
    st.markdown(f'<div class="hero"><h1>{title}</h1><p>{subtitle}</p></div>', unsafe_allow_html=True)


def product_card(name: str, price: str, category: str = "", image_url: str = "",
                 tag: str = "", emoji: str = "👗") -> None:
    """A rounded product card with hover lift. Pass image_url or it shows an emoji placeholder."""
    media = f'<img src="{image_url}" alt="{name}">' if image_url else f'<div class="ph">{emoji}</div>'
    tag_html = f'<span class="tag">{tag}</span>' if tag else ""
    st.markdown(
        f"""<div class="pcard">{media}<div class="body">
<div class="cat">{category}</div><p class="name">{name}</p>
<div class="row"><span class="price">{price}</span>{tag_html}</div></div></div>""",
        unsafe_allow_html=True,
    )
