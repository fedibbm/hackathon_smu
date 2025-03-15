# IMPORTS
import ollama
import logging

# REQUIRED_LIBRARIES
# No external libraries needed beyond ollama

def run():
    logging.basicConfig(level=logging.INFO)
    
    # AUTONOMOUS DATA COLLECTION
    try:
        with open("product_ideas.txt", "r") as f:
            ideas = f.read()
        logging.info(f"Read product ideas: {ideas}")
    except FileNotFoundError:
        logging.error("Product ideas file not found.")
        return "ERROR: product_ideas.txt not found."
    except Exception as e:
        logging.error(f"Error reading product ideas file: {e}")
        return "ERROR: Could not read product_ideas.txt."

    prompt = f"Provide constructive feedback on the following product ideas. Identify potential weaknesses, areas for improvement, and alternative approaches. Be specific and actionable: \n\n{ideas}"
    
    # LOCAL MODEL PROCESSING
    try:
        ollama.pull('llama2')  # Ensure model is available
        response = ollama.generate(model='llama2', prompt=prompt, stream=False)
        feedback = response['response']
        logging.info(f"Generated feedback: {feedback}")
    except Exception as e:
        logging.error(f"Error generating feedback: {e}")
        return "ERROR: Could not generate feedback."
    
    # AUTOMATED ACTION
    try:
        with open("product_feedback.txt", "w") as f:
            f.write(feedback)
        return "product_feedback.txt"
    except Exception as e:
        logging.error(f"Error writing to file: {e}")
        return "ERROR: Could not write to file."

if __name__ == "__main__":
    print(f"🚀 Starting {__file__}")
    result = run()
    print(f"✅ Completed: {result}")

