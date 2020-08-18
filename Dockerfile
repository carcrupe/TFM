FROM python:3.7
EXPOSE 8501/tcp
WORKDIR /app
COPY requirements/requirements_modeling.txt ./requirements_modeling.txt
COPY notebooks/best.model ./best.model
RUN pip install -r requirements_modeling.txt
COPY . .
CMD streamlit run stroke_visualization.py

