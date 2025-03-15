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
    
    try:
        with open("product_feedback.txt", "r") as f:
            feedback = f.read()
        logging.info(f"Read product feedback: {feedback}")
    except FileNotFoundError:
        logging.error("Product feedback file not found.")
        return "ERROR: product_feedback.txt not found."
    except Exception as e:
        logging.error(f"Error reading product feedback file: {e}")
        return "ERROR: Could not read product_feedback.txt."

    prompt = f"Refine the following product ideas based on the given feedback. Incorporate the suggestions and address the weaknesses identified. \n\nProduct Ideas:\n{ideas}\n\nFeedback:\n{feedback}"
    
    # LOCAL MODEL PROCESSING
    try:
        ollama.pull('llama2') 
        response = ollama.generate(model='llama2', prompt=prompt, stream=False)
        refined_ideas = response['response']
        logging.info(f"Generated refined ideas: {refined_ideas}")
    except Exception as e:
        logging.error(f"Error generating refined ideas: {e}")
        return "ERROR: Could not generate refined ideas."
    
    # AUTOMATED ACTION
    try:
        with open("refined_product_ideas.txt", "w") as f:
            f.write(refined_ideas)
        return "refined_product_ideas.txt"
    except Exception as e:
        logging.error(f"Error writing to file: {e}")
        return "ERROR: Could not write to file."

if __name__ == "__main__":
    print(f"🚀 Starting {__file__}")
    result = run()
    print(f"✅ Completed: {result}")

