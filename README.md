# AI Tutorials

Welcome to the **AI Tutorials** project! This repository contains various AI use cases and mini-projects, each exploring a unique functionality or concept in artificial intelligence. The goal is to provide practical, hands-on examples of AI applications, including chatbots, agents, memory management, and more.

## Project Structure

This project is organized into the following main directories:

```plaintext
ai_tutorials/
├── README.md                # Project overview and instructions
├── requirements.txt         # Dependencies
├── shared_lib/              # Common utilities shared across use cases
└── use_cases/               # Individual AI use cases
```

### Key Directories

- **`shared_lib/`**: Contains utilities and modules shared across various use cases, such as memory management tools, database connectors, and general-purpose utilities.
- **`use_cases/`**: Each subfolder here is an individual use case (e.g., simple agents, chatbots, chatbots with memory, chatbots with memory and database, etc.).

### Example Use Cases

Each folder in `use_cases/` is a standalone mini-project representing a unique AI use case. Here are a few examples:

- **`agents/`**: A simple AI agent demonstrating autonomous behavior.
- **`chatbot/`**: A basic chatbot implementation with interactive capabilities.
- **`chatbot_memory/`**: A chatbot that retains conversation memory across interactions.
- **`chatbot_memory_db/`**: An advanced chatbot that leverages both memory and database storage.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Required dependencies (install with `pip install -r requirements.txt`)

### Setting Up a Virtual Environment

It’s recommended to create a virtual environment to manage dependencies. Follow these steps:

1. Create the virtual environment:
    ```bash
    python3 -m venv env
    ```

2. Activate the environment:
   - On **Windows**:
       ```bash
       .\env\Scripts\activate
       ```
   - On **macOS/Linux**:
       ```bash
       source env/bin/activate
       ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/NSCarvalho/ai-tutorials.git
cd ai_tutorials
pip install -r requirements.txt
```

### Running a Use Case

Navigate to the `use_cases/` folder and choose the use case you want to run. Each use case has its own `*_app.py` entry point.

For example, to run the basic chatbot:

```bash
cd use_cases/agents
python custom_agent_app.py
```

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See `LICENSE` for more information.