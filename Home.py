import streamlit as st
import base64

st.set_page_config(page_title="CAN.D 플랫폼", layout="wide")

# 사이드바 네비게이션 강제 숨기기
st.markdown("""
<style>
/* 자동 생성된 사이드바 네비게이션 숨기기 */
[data-testid="stSidebarNav"] {
    display: none !important;
}
    [data-testid="stSidebar"] {
    background-color: #F5F0FA;  /* 연보라 */
}    
    .stApp {
    background-color: #F5F0FA;
    margin-left: -170px;  /* ✅ 핵심 */
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        .stApp {
            background-color: #F5F0FA;
        }
    </style>
""", unsafe_allow_html=True)

# # 상단 여백
# st.markdown("<br>", unsafe_allow_html=True)

# with open("organ/logo3.png", "rb") as f:
#     logo_base64 = base64.b64encode(f.read()).decode()

# # 가운데 정렬된 이미지 삽입
# st.markdown(f"""
#     <div style="text-align: center;">
#         <img src="data:image/png;base64,{logo_base64}" width="200">
#     </div>
# """, unsafe_allow_html=True)

# 이미지 → base64 인코딩 함수
def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# 세 이미지 인코딩
img_left = img_to_base64("분자구조식2.png")
img_center = img_to_base64("organ/logo3.png")
img_right = img_to_base64("분자구조식3.png")

# 세 개 나란히, 붙어서 가운데 정렬
st.markdown(f"""
    <div style="display: flex; justify-content: center; align-items: center; gap: 0px; margin-top: 30px;">
        <img src="data:image/png;base64,{img_left}" style="width: 100px; margin-right: -20px;" />
        <img src="data:image/png;base64,{img_center}" style="width: 200px; margin: 0 10px;" />
        <img src="data:image/png;base64,{img_right}" style="width: 100px; margin-left: -20px;" />
    </div>
""", unsafe_allow_html=True)

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Do+Hyeon&display=swap" rel="stylesheet">
<style>
h3 {
    font-family: 'Do Hyeon', sans-serif !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: center; margin-bottom: 80px;'>
        <h3 style='color: #4b0f70; font-family: "Nanum Gothic", sans-serif; font-size: 30px;'>
            <br><br>     CAN.D는 데이터 기반의 후보물질 선별과 약물 적응증 탐색을 지원합니다
        </h3>
        <h3 style='color: #4b0f70; font-family: "Nanum Gothic", sans-serif; font-size: 20px; font-weight : 300'> 
        세포주 유전체와 약물 구조 데이터를 통합하여, 전임상 단계에서 약물 반응성을 정량적으로 예측합니다.<br><br><br>
        </h3>  
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    # 파일을 base64로 인코딩
    def gif_to_base64(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()

    gif_base64 = gif_to_base64("dna_rotation_yaya.gif")

    # HTML 삽입
    st.markdown(f"""
        <div style="text-align: center; margin-top: 30px;">
            <img src="data:image/gif;base64,{gif_base64}" 
                style="width: 100%; opacity: 0.8; transform: rotate(30deg);" />
        </div>
    """, unsafe_allow_html=True)

with col2:
    subcol1, subcol2 = st.columns([1, 2])

    # with subcol1:
    #     img_str_base64 = img_to_base64("structure.png")
    #     st.markdown(f"""
    #         <div style="text-align: center; margin-top: 30px;">
    #             <img src="data:image/gif;base64,{img_str_base64}" 
    #                 style="width: 100%; opacity: 0.8; transform: rotate(30deg);" />
    #         </div>
    #     """, unsafe_allow_html=True)


    with subcol2:
        # 링크 구성
        st.markdown('<div class="card-container">', unsafe_allow_html=True)
        # st.markdown(f'<a class="card-link" href="pages/cell_line.py" target="_self">:dna: Cell Line</a>', unsafe_allow_html=True)
        # st.markdown(f'<a class="card-link" href="pages/Drug_info_page.py" target="_self">💊 Drug</a>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.page_link("pages/cell_line.py", label="🧬 Cell Line")
        st.markdown("</div>", unsafe_allow_html=True)
        st.page_link("pages/Drug.py", label="💊 Drug")
        st.markdown("</div>", unsafe_allow_html=True)
        st.page_link("pages/Indication.py", label="🩺 Indication")
        st.markdown("</div>", unsafe_allow_html=True)
        st.page_link("pages/Prediction.py", label="📈 Prediction")

    # 👉 CSS 정의
    st.markdown(f"""
    <style>
    .card-container {{
        display: flex;
        gap: 40px;
        flex-wrap: wrap;
        justify-content: flex-start;
        margin-left: 300px;   
        margin-top: 40px;
    }}

    .stPageLink {{
        display: flex;                         
        justify-content: center;
        align-items: center;

        width: 250px;                          
        height: 70px;
        background-color: #e6e6fa;             
        border-radius: 20px;
        font-size: 22px;
        font-weight: bold;
        color: #4c2a85 !important;
        text-decoration: none;
        box-shadow: 3px 3px 10px rgba(0,0,0,0.3);
        transition: all 0.3s ease-in-out;
        margin-left: -40px;
    }}

    .stPageLink:hover {{
        transform: scale(1.05);
        box-shadow: 5px 5px 15px rgba(0,0,0,0.5);
    }}
    </style>
    """, unsafe_allow_html=True)


# ✅ 각 이미지 경로와 연결할 링크 정의
image_links = [
    {"path": "kaggle.png", "url": "https://www.kaggle.com/datasets/samiraalipour/genomics-of-drug-sensitivity-in-cancer-gdsc"},
    {"path": "gdsc.png", "url": "https://www.cancerrxgene.org/"},
    {"path": "snager.png", "url": "https://www.sanger.ac.uk/"},
    {"path": "mgh.png", "url": "https://www.massgeneral.org/cancer-center?cmp=cared&utm_source=redirect&utm_medium=offline&utm_campaign=mgb-cancer"}
]

# ✅ HTML 생성
html = """
<hr style="margin-top: 300px; margin-bottom: 30px; border: none; border-top: 2px solid #ccc;">
<div style="display: flex; justify-content: flex-start; gap: 0; margin-left: 120px;">
"""

for item in image_links:
    b64_img = img_to_base64(item["path"])
    if item["path"] == "gdsc.png":
        width = "30%"  
    else:
        width = "35%"  

    img_tag = f'<img src="data:image/png;base64,{b64_img}" style="width: {width}; border-radius: 8px; margin: 50px; padding: 0; display: block;">'

    if item["url"]:
        html += f'<a href="{item["url"]}" target="_blank" style="margin: 0; padding: 0;">{img_tag}</a>'
    else:
        html += img_tag

html += '</div></div>'
st.markdown(html, unsafe_allow_html=True)