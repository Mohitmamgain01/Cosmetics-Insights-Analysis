from flask import Flask, render_template

app = Flask(__name__)

CONFIG = {

    "tableau_dashboard_workbook": "Cosmetics_insights_analysisDashboard",
    "tableau_dashboard_view": "Dashboard-CosmeticsInsights",
    "tableau_story_workbook": "Cosmetics_insights_analysisStory",
    "tableau_story_view": "Story-CosmeticsInsights",

    "tableau_profile_url": "https://public.tableau.com/app/profile/mohit.mamgain6376/vizzes",
    "github_repo_url": "https://github.com/yourusername/Cosmetics-Insights-Analysis",

    # ---- Headline content ----
    "project_title": "Cosmetics Insights Analysis",
    "project_tagline": "A Tableau dashboard that looks at cosmetics product data — "
                        "prices, brands, categories, and which skin types each "
                        "product is made for.",

    # ---- KPI values ----
   
    "kpis": [
        {"label": "Total Products", "value": "1,472", "tone": "gold"},
        {"label": "Total Brands", "value": "126", "tone": "rose"},
        {"label": "Skin Types Covered", "value": "5", "tone": "gold"},
    ],

    # ---- About section ----
    "dataset_description": (
        "A cosmetics product dataset with brand, product name, category, "
        "ingredients, price, and ranking, plus which skin types (combination, "
        "dry, normal, oily, sensitive) each product is suited for."
    ),
    "tools_used": ["Tableau Public", "Flask", "GitHub"],
    "authors": ["Mohit Mamgain"],

}


def build_tableau_embed(div_id, workbook, view):
    """
    Builds everything the classic Tableau Public embed snippet needs
    (the same one you get from Share -> Embed Code on Tableau Public),
    from just a workbook name and a view name.
    """
    name = f"{workbook}/{view}"
    prefix = workbook[:2]  # matches the 2-letter folder Tableau uses, e.g. "Co"
    base = f"https://public.tableau.com/static/images/{prefix}/{workbook}/{view}"
    return {
        "div_id": div_id,
        "name": name,
        "static_image": f"{base}/1.png",
        "rss_image": f"{base}/1_rss.png",
        "view_url": f"https://public.tableau.com/views/{name}",
    }


@app.route("/")
def home():
    embeds = {
        "dashboard": build_tableau_embed(
            "vizDashboard", CONFIG["tableau_dashboard_workbook"], CONFIG["tableau_dashboard_view"]
        ),
        "story": build_tableau_embed(
            "vizStory", CONFIG["tableau_story_workbook"], CONFIG["tableau_story_view"]
        ),
    }
    return render_template("index.html", cfg=CONFIG, embeds=embeds)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5500, debug=True)
