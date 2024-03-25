# Nephrotic Syndrom Insight AI 
A Retriever-Augmented Generation Model for Nephrotic Syndrome Literature
## Overview
NSinsight is a dedicated repository created to host an advanced Retriever-Augmented Generation (RAG) model, specifically designed to navigate the complex landscape of Nephrotic Syndrome (NS) research. Our mission is to transform the accessibility and understanding of scientific literature related to NS, making it easier for researchers, clinicians, and caregivers to find precise, comprehensive, and up-to-date insights about this challenging condition.

## Objectives
Synthesize Key Information: To aggregate and synthesize information from a wide array of research papers, clinical studies, and review articles focused on Nephrotic Syndrome, including its subtypes such as Steroid-Dependent Nephrotic Syndrome (SDNS) and Frequent Relapse Nephrotic Syndrome (FRNS).
Facilitate Advanced Queries: To enable users to perform sophisticated queries that return nuanced insights and information, assisting in understanding treatment options, management strategies, and the latest research findings.
Support Decision Making: To aid in clinical decision-making and patient care planning by providing access to the latest evidence-based information and treatment outcomes for Nephrotic Syndrome.

## Methodology
The NSinsight repository implements a RAG model combining the strengths of a dense vector retriever and a powerful generative transformer. This approach allows for real-time retrieval of relevant information from a curated dataset of scientific papers on Nephrotic Syndrome, followed by the generation of coherent, contextually relevant summaries and answers to user queries.

## Data Collection
The foundation of NSinsight is a comprehensive dataset comprising recent papers, articles, and reviews related to Nephrotic Syndrome. These documents are meticulously indexed using LAMAindex to ensure efficient and accurate retrieval.

## Model Implementation
Our RAG model leverages this indexed dataset to answer complex queries about NS. By extracting relevant information from the indexed papers in real-time, the model generates detailed, accurate responses that reflect the latest research and clinical guidelines.

## Impact
NSinsight aims to democratize access to specialized knowledge on Nephrotic Syndrome, offering a novel tool for medical professionals, researchers, and families affected by NS. By streamlining the process of extracting information from extensive literature, NSinsight supports informed decision-making, promotes personalized care, and fosters ongoing research into Nephrotic Syndrome.

# How to use
* run `pip install -r requirements.txt`
* copy all your pdf to ./data
* copy .dev.env to .env and update OpenAI key
* run `python index_pdfs.py`
* run `python app.py`  #to use web interface
* run 'python simple_ask.py'  #to ask a simple question