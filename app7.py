import streamlit as st

st.set_page_config(
    page_title="Calorie Calculator",
    page_icon="🥗",
    layout="centered"
)

st.title("🥗 Daily Calorie Calculator")
st.write("Calculate your estimated daily calorie requirement.")

st.divider()

st.subheader("👤 Personal Details")

age = st.number_input(
    "Age",
    min_value=10,
    max_value=100,
    value=21
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

weight = st.number_input(
    "Weight (kg)",
    min_value=20.0,
    max_value=200.0,
    value=60.0
)

height = st.number_input(
    "Height (cm)",
    min_value=100.0,
    max_value=220.0,
    value=165.0
)

st.divider()

st.subheader("🏃 Activity Level")

activity = st.selectbox(
    "Select your activity level",
    [
        "Sedentary - Little or no exercise",
        "Lightly Active - Exercise 1-3 days/week",
        "Moderately Active - Exercise 3-5 days/week",
        "Very Active - Exercise 6-7 days/week",
        "Extra Active - Hard exercise or physical job"
    ]
)

activity_factor = {
    "Sedentary - Little or no exercise": 1.2,
    "Lightly Active - Exercise 1-3 days/week": 1.375,
    "Moderately Active - Exercise 3-5 days/week": 1.55,
    "Very Active - Exercise 6-7 days/week": 1.725,
    "Extra Active - Hard exercise or physical job": 1.9
}

st.divider()

if st.button(
    "🥗 Calculate Calories",
    use_container_width=True
):

    # BMR calculation
    if gender == "Male":
        bmr = (
            10 * weight
            + 6.25 * height
            - 5 * age
            + 5
        )
    else:
        bmr = (
            10 * weight
            + 6.25 * height
            - 5 * age
            - 161
        )

    # Daily calorie requirement
    calories = bmr * activity_factor[activity]

    st.success("✅ Calculation completed!")

    st.subheader("📊 Your Result")

    st.metric(
        "Estimated Daily Calories",
        f"{calories:.0f} kcal/day"
    )

    st.write(
        f"**BMR:** {bmr:.0f} kcal/day"
    )

    st.write(
        f"**Activity Level:** {activity}"
    )

    st.divider()

    st.info(
        "💡 This is an estimated calorie requirement "
        "based on the information provided."
    )

    if calories < 1800:
        st.write(
            "🥗 Your estimated requirement is relatively low. "
            "Focus on balanced and nutritious meals."
        )

    elif calories < 2500:
        st.write(
            "🥗 Your estimated requirement is in a moderate range. "
            "Maintain a balanced diet and regular activity."
        )

    else:
        st.write(
            "🏃 Your estimated requirement is relatively high. "
            "Make sure your meals provide enough nutrients and energy."
        )

    st.caption(
        "Note: This calculator provides an estimate and is not medical advice."
    )