import shap

def explain_with_shap(model, input_sample):
    explainer = shap.Explainer(model)
    shap_values = explainer(input_sample)
    shap.plots.waterfall(shap_values[0])
