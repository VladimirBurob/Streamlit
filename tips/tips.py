import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.title("Анализ чаевых (tips dataset)")
st.sidebar.title("Настройки")
tips = "/Users/vladimir/Desktop/ds_bootcamp/week2_3-4/vis/tips.csv"
uploaded_file = st.sidebar.file_uploader("Загрузите CSV файл", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    try:
        df = pd.read_csv(tips)
    except FileNotFoundError:
        st.error(f"Файл не найден по пути: {tips}")
        st.stop()

st.sidebar.write("Первые 5 строк датасета:")
st.sidebar.dataframe(df.head())

chart_type = st.sidebar.selectbox(
    "Выберите тип графика",
    ("Гистограмма", "Boxplot", "Scatter plot", "Bar chart", "Line chart")
)

gender_filter = st.sidebar.multiselect(
    "Фильтр по полу",
    options=df["sex"].unique(),
    default=df["sex"].unique()
)

filtered_df = df[df["sex"].isin(gender_filter)]
if chart_type == "Гистограмма":
    st.write("### Гистограмма распределения общего счета")
    fig, ax = plt.subplots()
    sns.histplot(filtered_df["total_bill"], kde=True, ax=ax)
    st.pyplot(fig)

elif chart_type == "Boxplot":
    st.write("### Boxplot чаевых по дням недели")
    fig, ax = plt.subplots()
    sns.boxplot(x="day", y="tip", data=filtered_df, ax=ax)
    st.pyplot(fig)

elif chart_type == "Scatter plot":
    st.write("### Scatter plot: общий счет vs чаевые")
    fig, ax = plt.subplots()
    sns.scatterplot(x="total_bill", y="tip", hue="sex", data=filtered_df, ax=ax)
    st.pyplot(fig)

elif chart_type == "Bar chart":
    st.write("### Bar chart: средние чаевые по времени суток")
    bar_data = filtered_df.groupby("time")["tip"].mean()
    st.bar_chart(bar_data)

elif chart_type == "Line chart":
    st.write("### Line chart: общая сумма счетов по дням недели")
    line_data = filtered_df.groupby("day")["total_bill"].sum()
    st.line_chart(line_data)

if st.sidebar.button("Скачать график"):
    fig, ax = plt.subplots()
    sns.histplot(filtered_df["total_bill"], kde=True, ax=ax)
    plt.savefig("plot.png")
    with open("plot.png", "rb") as file:
        btn = st.sidebar.download_button(
            label="Скачать график",
            data=file,
            file_name="plot.png",
            mime="image/png"
        )

st.write("### Основная статистика датасета")
st.dataframe(filtered_df.describe())