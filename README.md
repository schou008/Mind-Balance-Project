# Mind Balance  
### Lifestyle-Based Mental Health Insight Tool

## Live Demo

A fully functional version of the Mind Balance system is available online:
https://mind-balance-project-kdx7bs6wjyg7hthspr6xrq.streamlit.app/

This live demo allows users to:
- Input lifestyle data (sleep, screen time, exercise, social interaction)
- Receive a real-time mental health risk prediction
- View an overall wellbeing score (0–100)
- Explore AI-driven explainability insights
- Access personalised recommendations based on their inputs

The deployed application demonstrates the core functionality of the system end-to-end and reflects the implementation described in this repository.

## Project Overview

Mind Balance is an online intelligent decision-support system aimed at assessing mental health risks based on lifestyle patterns typically linked to student wellbeing. The system evaluates essential behavioural indicators such as sleep duration, screen time, physical activity and social interaction to produce a predicted risk classification along with an overall wellbeing score.

This project merges machine learning, explainable artificial intelligence and user-centred design principles to develop an accessible tool that enhances awareness of mental health risk factors. Rather than serving as a diagnostic tool, Mind Balance is intended as a reflective and educational platform that motivates users to reflect on how their daily habits may affect their psychological wellbeing.

A significant feature of the system is its interpretability. In contrast to many  machine learning applications, Mind Balance incorporates SHAP-based explanations to offer clarity on how individual inputs influence predictions. This guarantees that users receive not only a result but also an understanding of the rationale behind it.

The system is presented through a lightweight interactive web interface created with Streamlit, facilitating real-time user engagement, prompt feedback and visual representation of outcomes.

## Project Aim

The primary aim of this project is to design and implement an interpretable machine learning system that can provide early-stage mental health risk insights based on lifestyle data in a non-clinical context.

More specifically, the project aims to:

- Investigate the relationship between lifestyle behaviours and mental wellbeing indicators  
- Develop a predictive model capable of classifying mental health risk levels using behavioural data  
- Integrate explainable AI techniques to ensure transparency and user trust in model outputs  
- Design a user-friendly interface that supports accessibility and reduces cognitive complexity  
- Encourage self-awareness and proactive reflection on lifestyle choices among university students  

This project also seeks to connect technical machine learning systems with practical usability by prioritising not just predictive accuracy but also interpretability, usability and ethical considerations. The focus is on facilitating informed self-reflection instead of offering clinical diagnoses or psychological evaluations.

## Core Features

- Machine learning-based mental health risk classification  
- Lifestyle-based health score (0–100)  
- Explainable AI (SHAP) to interpret model decisions  
- Personalised lifestyle recommendations  
- Visual breakdown of risk factors  
- Interactive dashboard interface  


## Machine Learning Approach

The system uses a Random Forest Classifier trained on synthetic lifestyle data. Features include:

- Sleep duration  
- Screen time  
- Exercise levels  
- Social interaction  

The model outputs a categorical risk level representing estimated mental wellbeing.

## Explainable AI (SHAP)

SHAP is used to improve model transparency by showing how each input feature contributes to the final prediction. This allows users to understand the reasoning behind their risk classification and increases interpretability of machine learning outputs.

## System Design

The system follows a User-Centred Design (UCD) approach with emphasis on:

- Simplicity and clarity of interaction  
- Non-clinical, supportive language  
- Minimal cognitive load for users  
- Accessible dashboard-based interface  

## System Architecture

The application is structured using a modular approach:

- Frontend Layer: Streamlit interface for user interaction  
- Logic Layer: Python-based processing and scoring system  
- Model Layer: Machine learning classifier with SHAP explainability  

This separation improves maintainability and scalability of the system.

## Ethical Considerations

- The system is explicitly non-diagnostic  
- No permanent storage of sensitive personal data  
- Designed for educational and awareness purposes only  
- Outputs are intended for reflection, not medical interpretation  

## Limitations

- Uses synthetic training data rather than clinical datasets  
- Limited number of behavioural input features  
- Predictions are indicative and not medically validated  
- SHAP outputs are simplified for interpretability  
- No longitudinal tracking of user behaviour  

## Future Enhancements

- Integration with real-world datasets  
- Improved model accuracy and validation  
- Expanded behavioural indicators (diet, stress, academics)  
- Personal user tracking and history analysis  
- Advanced explainability visualisations  

## Technologies Used

- Python  
- Streamlit  
- Scikit-learn  
- Pandas / NumPy  
- SHAP  
- SQLite  
- Machine Learning (Random Forest)  
- matplotlib
- joblib
- reportlab

## Summary

Mind Balance illustrates the utilisation of machine learning and explainable artificial intelligence within a human-focused digital wellbeing framework. The system effectively combines predictive modelling with interpretability methods to create an accessible tool that converts intricate behavioural data into significant and comprehensible insights.

The final system offers users a risk classification (Low, Moderate, High), a computed wellbeing score, visual representations of contributing lifestyle factors and tailored recommendations aimed at promoting healthier behavioural patterns. By employing SHAP explainability, the system improves transparency by demonstrating how each input feature influences the final prediction.

From a design standpoint, the project embraces a user-centred and ethically conscious approach, ensuring that outputs are delivered in a supportive and non-clinical fashion. This is especially crucial in sensitive areas such as mental health, where clarity, trust and responsible communication are vital.

In summary, the project showcases how machine learning systems can be tailored for educational and preventative wellbeing purposes, while preserving interpretability, usability and ethical integrity. It underscores the potential for AI-driven tools to facilitate early awareness and reflection in mental health without supplanting professional healthcare services.