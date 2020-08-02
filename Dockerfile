FROM python:3.7
EXPOSE 8501
WORKDIR /app
COPY requirements_modeling.txt ./requirements_modeling.txt
RUN pip install -r requirements_modeling.txt
COPY . .
CMD streamlit run stroke_visualization.py

