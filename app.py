import streamlit as st
import os
import datetime
import yaml
from overview_dataset import OverviewDataset
from variables import Variable
from advice import ChatGpt
from correlation import Correlation
from more_plot import MorePlot

with open("api.yaml", encoding="UTF-8") as f:
    cfg = yaml.load(f, Loader=yaml.FullLoader)
with open("prompt.yaml", encoding="UTF-8") as f:
    prompt = yaml.load(f, Loader=yaml.FullLoader)


def save_uploaded_file(directory, file):
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(os.path.join(directory, file.name), "wb") as f:
        f.write(file.getbuffer())
    return st.success("파일 업로드 성공!")


def service_1(filename):
    path = "csv/" + filename
    st.header(":hash: 데이터셋 개요", divider="rainbow")
    over = OverviewDataset(path)
    Chat = ChatGpt(cfg["api_key"])
    col1, col2 = st.columns([3, 5])
    with col1:
        st.subheader(":memo: statistic", divider="gray")
        st.dataframe(over.generate_summary_dict())
    with col2:
        st.subheader(":exclamation: advice", divider="gray")
        st.text_area(
            "advice",
            Chat.generate_advice(
                prompt["prompt_overview"], over.generate_summary_sentence()
            ),
            height=300,
            max_chars=1500,
            label_visibility="collapsed",
        )


def service_2(filename):
    path = "csv/" + filename
    st.header(":hash: 변수", divider="rainbow")
    var = Variable(path)
    Chat = ChatGpt(cfg["api_key"])
    num_variables = var.num_var
    for idx in range(num_variables):
        st.text(f"◼️ 변수명: {var.columns[idx]}")
        tab1, tab2, tab3 = st.tabs(
            [":memo: statistic", "📈 chart", ":exclamation: advice"]
        )
        with tab1:
            st.dataframe(var.variable_statistic(idx))
        with tab2:
            var.variable_plot(idx)
            st.image(f"variable/plot{idx}.png")
        with tab3:
            st.text_area(
                "advice",
                Chat.generate_advice(prompt["prompt_var"], var.variable_sentence(idx)),
                height=300,
                max_chars=1500,
                label_visibility="collapsed",
            )


def service_3(filename):
    path = "csv/" + filename
    st.header(":hash: 상관관계", divider="rainbow")
    corr = Correlation(path)
    Chat = ChatGpt(cfg["api_key"])
    col1, col2 = st.columns([3, 5])
    with col1:
        st.subheader("📈 chart", divider="gray")
        corr.plot_correlation()
        st.image("correlation/heatmap.png")
    with col2:
        st.subheader(":exclamation: advice", divider="gray")
        st.text_area(
            "advice",
            Chat.generate_advice(
                prompt["prompt_corr"], corr.generate_correlation_sentence()
            ),
            height=300,
            max_chars=1500,
            label_visibility="collapsed",
        )


def service_4(filename):
    path = "csv/" + filename
    st.header(":hash: 시각화 도구", divider="rainbow")
    text_input = st.text_input(
        "어떻게 차트를 생성할지 입력하세요 👇",
        placeholder="입력란",
    )
    col1, col2 = st.tabs(["📈 chart", ":exclamation: advice"])
    more_plot = MorePlot(cfg["api_key"])
    Chat = ChatGpt(cfg["api_key"])
    if text_input:
        more_plot.generate_plot(path, text_input)
        sentence = more_plot.generate_sentence()
    with col1:
        if text_input:
            st.image("exports/charts/temp_chart.png")
    with col2:
        if text_input:
            st.text_area(
                "advice",
                Chat.generate_advice(prompt["prompt_chart"], sentence),
                height=300,
                max_chars=1500,
                label_visibility="collapsed",
            )


def main():
    st.title("Welcome to AI-advisor!  :wave:")
    menu = ["main", "준비중"]
    choice = st.sidebar.selectbox("메뉴", menu)
    filename = None
    if choice == menu[0]:
        csv_file = st.file_uploader(":warning: csv 파일을 업로드 하세요!", type=["csv"])
        if csv_file is not None:
            current_time = datetime.datetime.now()
            filename = current_time.isoformat().replace(":", "_") + ".csv"
            csv_file.name = filename
            save_uploaded_file("csv", csv_file)
            service_1(filename)
            service_2(filename)
            service_3(filename)
            service_4(filename)


if __name__ == "__main__":
    main()
