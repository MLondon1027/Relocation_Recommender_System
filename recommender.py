from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import streamlit as st


def cosine_recommend_zip(zip_input, num, city, state):

    if state:
        state = state.upper()

    if city:
        city = city.title()

    if not num:
        num = 10

    # Load data
    final = pd.read_csv("final_data.csv")

    final["index"] = final["index"].astype(str).str.zfill(5)

    # Remove unnecessary columns if they exist
    final.drop(
        columns=["Unnamed: 0", "level_0"],
        inplace=True,
        errors="ignore"
    )

    final.set_index("index", inplace=True)

    # Scale data
    scaler = StandardScaler()
    scaled = scaler.fit_transform(final)

    scaled = pd.DataFrame(
        scaled,
        index=final.index,
        columns=final.columns
    )

    # Check ZIP
    if zip_input not in scaled.index:
        return None, "Please enter a valid ZIP code."

    # Find index of ZIP
    zip_index = scaled.index.get_loc(zip_input)

    # Calculate cosine similarity
    cosine_scores = cosine_similarity(
        scaled.iloc[[zip_index]],
        scaled
    )[0]

    # Sort ZIP codes by similarity
    zip_indices = cosine_scores.argsort()[::-1]

    best_zips = final.index[zip_indices]

    df = pd.DataFrame({
        "Zip": best_zips.astype(int)
    })

    # Load ZIP location data
    zip_location = pd.read_csv(
        "us-zip-code-latitude-and-longitude.csv",
        sep=";"
    )

    merged = pd.merge(
        df,
        zip_location,
        on="Zip",
        how="inner"
    )

    merged = merged[["Zip", "City", "State"]]

    # Remove input ZIP itself
    merged = merged[merged["Zip"] != int(zip_input)]

    # Optional state filter
    if state:
        merged = merged[merged["State"] == state]

    # Optional city filter
    if city:
        if not state:
            return None, "You must enter a state when entering a city."

        merged = merged[
            merged["City"].str.lower() == city.lower()
        ]

    merged = merged.reset_index(drop=True)

    if merged.empty:
        return None, "No matching recommendations found."

    return merged.head(int(num)), None


# --------------------------
# STREAMLIT APP
# --------------------------

st.title("Relocation Recommender System")

st.write(
    "Enter your current ZIP code to find similar places to live."
)

zip_input = st.text_input(
    "ZIP Code",
    max_chars=5
)

num = st.number_input(
    "Number of recommendations",
    min_value=1,
    max_value=50,
    value=10
)

state = st.text_input(
    "State abbreviation (optional)",
    max_chars=2
)

city = st.text_input(
    "City (optional)"
)

if st.button("Find Recommendations"):

    if not zip_input:
        st.error("Please enter a ZIP code.")

    elif not zip_input.isdigit() or len(zip_input) != 5:
        st.error("Please enter a valid 5-digit ZIP code.")

    else:
        with st.spinner("Finding similar ZIP codes..."):

            recommendations, error = cosine_recommend_zip(
                zip_input,
                num,
                city,
                state
            )

        if error:
            st.error(error)

        else:
            st.success(
                f"Top {len(recommendations)} recommendations"
            )

            st.dataframe(
                recommendations,
                hide_index=True,
                use_container_width=True
            )
