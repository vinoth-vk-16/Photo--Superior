import gradio as gr
import colorizer  # Import colorizer module
# Import enhancer module


def create_home_page():
    """Create the home page."""
    return gr.HTML("<h1>Welcome to Photo Superior</h1><p>Select a tab to get started.</p>")


def create_tabs():
    
    with gr.Blocks() as app:
        with gr.Tabs():
            with gr.TabItem("Home"):
                create_home_page()
            with gr.TabItem("Image Colorizer"):
                colorizer.create_colorizer_page()
    app.launch(share=True)


if __name__ == "__main__":
    create_tabs()
