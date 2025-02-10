from setuptools import setup, find_packages

setup(
    name="crypto_forecast",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.85.0",
        "uvicorn>=0.19.0",
        "pandas>=1.4.3",
        "requests>=2.28.1",
        "prophet>=1.1.0",
        "scikit-learn>=1.1.2",
        "joblib>=1.2.0",
        "python-multipart>=0.0.5",
        "PyYAML>=6.0",
    ],
)
