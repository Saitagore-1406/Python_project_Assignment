import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(page_title="Calculator", page_icon="🧮", layout="centered")

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@300;400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

/* Dark background */
.stApp {
    background: #0f0f11;
    color: #e8e8ec;
}

h1, h2, h3 {
    font-family: 'Space Mono', monospace !important;
}

/* Title */
.calc-title {
    font-family: 'Space Mono', monospace;
    font-size: 2rem;
    font-weight: 700;
    color: #c8ff57;
    letter-spacing: -1px;
    margin-bottom: 0;
}

.calc-subtitle {
    font-family: 'DM Sans', sans-serif;
    font-weight: 300;
    color: #666;
    font-size: 0.85rem;
    margin-bottom: 2rem;
}

/* Result display box */
.result-box {
    background: #1a1a1f;
    border: 1px solid #2a2a35;
    border-left: 4px solid #c8ff57;
    border-radius: 8px;
    padding: 1.2rem 1.5rem;
    font-family: 'Space Mono', monospace;
    font-size: 2rem;
    color: #c8ff57;
    margin: 1rem 0;
    min-height: 70px;
    display: flex;
    align-items: center;
}

/* History items */
.history-item {
    background: #1a1a1f;
    border: 1px solid #222230;
    border-radius: 6px;
    padding: 0.5rem 1rem;
    margin: 0.3rem 0;
    font-family: 'Space Mono', monospace;
    font-size: 0.85rem;
    color: #aaa;
    display: flex;
    justify-content: space-between;
}

.history-item span.val {
    color: #e8e8ec;
    font-weight: 700;
}

/* Error / info boxes */
.msg-error {
    background: #2a1018;
    border-left: 3px solid #ff4d6a;
    border-radius: 6px;
    padding: 0.6rem 1rem;
    color: #ff4d6a;
    font-size: 0.85rem;
    font-family: 'DM Sans', sans-serif;
}

.msg-info {
    background: #101a10;
    border-left: 3px solid #57ff8c;
    border-radius: 6px;
    padding: 0.6rem 1rem;
    color: #57ff8c;
    font-size: 0.85rem;
}

/* Section labels */
.section-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.7rem;
    color: #555;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}

/* Operator badges */
.op-badge {
    display: inline-block;
    background: #1e1e28;
    border: 1px solid #333;
    border-radius: 4px;
    padding: 2px 8px;
    font-family: 'Space Mono', monospace;
    font-size: 0.85rem;
    color: #c8ff57;
    margin-right: 4px;
}

/* Streamlit widget overrides */
div[data-testid="stSelectbox"] label,
div[data-testid="stNumberInput"] label,
div[data-testid="stTextInput"] label {
    color: #888 !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.75rem !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
}

div[data-testid="stSelectbox"] > div > div,
div[data-testid="stNumberInput"] input,
div[data-testid="stTextInput"] input {
    background: #1a1a1f !important;
    border: 1px solid #2a2a35 !important;
    color: #e8e8ec !important;
    font-family: 'Space Mono', monospace !important;
    border-radius: 6px !important;
}

div[data-testid="stSelectbox"] > div > div:focus-within,
div[data-testid="stNumberInput"] input:focus,
div[data-testid="stTextInput"] input:focus {
    border-color: #c8ff57 !important;
    box-shadow: 0 0 0 2px rgba(200,255,87,0.15) !important;
}

/* Buttons */
.stButton > button {
    background: #c8ff57 !important;
    color: #0f0f11 !important;
    font-family: 'Space Mono', monospace !important;
    font-weight: 700 !important;
    border: none !important;
    border-radius: 6px !important;
    padding: 0.5rem 1.5rem !important;
    font-size: 0.85rem !important;
    letter-spacing: 0.5px !important;
    transition: opacity 0.15s !important;
}

.stButton > button:hover {
    opacity: 0.85 !important;
}

/* Secondary / danger buttons */
.stButton.secondary > button {
    background: #1e1e28 !important;
    color: #888 !important;
    border: 1px solid #333 !important;
}

div[data-testid="column"] .stButton > button {
    width: 100%;
}

/* Divider */
hr {
    border-color: #222230 !important;
    margin: 1.5rem 0 !important;
}

/* Hide Streamlit default elements */
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ── Session state init ────────────────────────────────────────────────────────
if "history" not in st.session_state:
    st.session_state.history = []       # list of (expr_str, result)
if "previous" not in st.session_state:
    st.session_state.previous = None
if "result" not in st.session_state:
    st.session_state.result = None
if "error" not in st.session_state:
    st.session_state.error = None

# ── Helper: validate number string ───────────────────────────────────────────
def check(n: str) -> bool:
    if n == "":
        return False
    dot = 0
    i = 0
    if n[0] == "-":
        if len(n) == 1:
            return False
        i = 1
    for j in range(i, len(n)):
        if n[j] == ".":
            dot += 1
            if dot > 1:
                return False
        elif n[j] < "0" or n[j] > "9":
            return False
    return True

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown('<div class="calc-title">// CALCULATOR</div>', unsafe_allow_html=True)
st.markdown('<div class="calc-subtitle">arithmetic operations · history · chaining</div>', unsafe_allow_html=True)

# ── Result display ────────────────────────────────────────────────────────────
if st.session_state.result is not None:
    st.markdown(
        f'<div class="result-box">= {st.session_state.result:g}</div>',
        unsafe_allow_html=True
    )
elif st.session_state.previous is not None:
    st.markdown(
        f'<div class="result-box" style="color:#555;">prev: {st.session_state.previous:g}</div>',
        unsafe_allow_html=True
    )
else:
    st.markdown('<div class="result-box" style="color:#333;">ready</div>', unsafe_allow_html=True)

if st.session_state.error:
    st.markdown(f'<div class="msg-error">⚠ {st.session_state.error}</div>', unsafe_allow_html=True)

st.markdown("---")

# ── Input form ────────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">Operation</div>', unsafe_allow_html=True)

OPERATORS = ["+", "−", "×", "%", "**"]
OP_MAP    = {"+": "+", "−": "-", "×": "*", "%": "%", "**": "**"}

op_display = st.selectbox("Operator", OPERATORS, label_visibility="collapsed")
operator   = OP_MAP[op_display]

col1, col2 = st.columns(2)

prev_label = ""
if st.session_state.previous is not None:
    prev_label = f"  (prev = {st.session_state.previous:g})"

with col1:
    st.markdown('<div class="section-label">First number</div>', unsafe_allow_html=True)
    num1_raw = st.text_input(
        f"First number{prev_label}",
        placeholder=f"number or 'p'{prev_label}",
        label_visibility="collapsed",
        key="num1"
    )

with col2:
    st.markdown('<div class="section-label">Second number</div>', unsafe_allow_html=True)
    num2_raw = st.text_input(
        f"Second number{prev_label}",
        placeholder=f"number or 'p'{prev_label}",
        label_visibility="collapsed",
        key="num2"
    )

if st.session_state.previous is not None:
    st.markdown(
        f'<div class="msg-info" style="font-size:0.78rem;">💡 Type <b>p</b> in either field to use the previous result ({st.session_state.previous:g})</div>',
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

calc_col, clear_col = st.columns([3, 1])

with calc_col:
    calculate = st.button("CALCULATE", use_container_width=True)

with clear_col:
    clear_hist = st.button("CLEAR", use_container_width=True)

# ── Calculate ─────────────────────────────────────────────────────────────────
if calculate:
    st.session_state.error  = None
    st.session_state.result = None

    # resolve num1
    if num1_raw.strip().lower() == "p":
        if st.session_state.previous is None:
            st.session_state.error = "No previous result to use."
            st.rerun()
        num1 = st.session_state.previous
    else:
        if not check(num1_raw.strip()):
            st.session_state.error = f"'{num1_raw}' is not a valid number."
            st.rerun()
        num1 = float(num1_raw.strip())

    # resolve num2
    if num2_raw.strip().lower() == "p":
        if st.session_state.previous is None:
            st.session_state.error = "No previous result to use."
            st.rerun()
        num2 = st.session_state.previous
    else:
        if not check(num2_raw.strip()):
            st.session_state.error = f"'{num2_raw}' is not a valid number."
            st.rerun()
        num2 = float(num2_raw.strip())

    # perform operation
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "%":
        if num2 == 0:
            st.session_state.error = "Cannot modulo by zero."
            st.rerun()
        result = num1 % num2
    elif operator == "**":
        result = num1 ** num2
    else:
        st.session_state.error = "Unknown operator."
        st.rerun()

    # format a nice expression string
    n1_str = f"prev({num1:g})" if num1_raw.strip().lower() == "p" else f"{num1:g}"
    n2_str = f"prev({num2:g})" if num2_raw.strip().lower() == "p" else f"{num2:g}"
    expr   = f"{n1_str} {op_display} {n2_str}"

    st.session_state.result   = result
    st.session_state.previous = result
    st.session_state.history.append((expr, result))
    st.rerun()

# ── Clear history ─────────────────────────────────────────────────────────────
if clear_hist:
    st.session_state.history  = []
    st.session_state.previous = None
    st.session_state.result   = None
    st.session_state.error    = None
    st.rerun()

# ── History panel ─────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown('<div class="section-label">History</div>', unsafe_allow_html=True)

if not st.session_state.history:
    st.markdown('<div style="color:#444; font-size:0.85rem; font-family: Space Mono, monospace;">no calculations yet</div>', unsafe_allow_html=True)
else:
    for i, (expr, val) in enumerate(reversed(st.session_state.history), 1):
        idx = len(st.session_state.history) - i + 1
        st.markdown(
            f'<div class="history-item">'
            f'<span style="color:#555;">#{idx:02d} &nbsp; {expr}</span>'
            f'<span class="val">= {val:g}</span>'
            f'</div>',
            unsafe_allow_html=True
        )
