from fasthtml.common import *

def render_main_page():
    return Div(
        Div(
            Div(
                H1('AI Image Generator'),
                Form(
                    Div(
                        Label('Enter Your FAL API Key:'),
                        Input(type='password', name='fal_key', placeholder='Paste your FAL key here'),
                        _class='form-group'
                    ),
                    Div(
                        Label('Enter Your Prompt:'),
                        Input(type='text', name='prompt', placeholder='e.g., photo of a rhino dressed in a suit and tie...'),
                        _class='form-group'
                    ),
                    Div(
                        Label('Image Size:'),
                        Select(
                            Option('landscape_4_3', value='landscape_4_3'),
                            Option('square_hd', value='square_hd'),
                            Option('square', value='square'),
                            Option('portrait_4_3', value='portrait_4_3'),
                            Option('portrait_16_9', value='portrait_16_9'),
                            Option('landscape_16_9', value='landscape_16_9'),
                            name='image_size'
                        ),
                        _class='form-group'
                    ),
                    Div(
                        Label('Number of Inference Steps:'),
                        Input(type='range', name='num_inference_steps', min='0', max='36', value='0', 
                              oninput='updateInferenceSteps(this.value)'),
                        Span('0', id='numInferenceStepsDisplay', style='margin-left: 10px;'),
                        _class='form-group'
                    ),
                    Div(
                        Label('Seed:'),
                        Div(
                            Input(type='number', name='seed', id='seedInput', placeholder='random', value=''),
                            Button('↻', type='button', _class='randomize-btn', onclick='randomizeSeed()'),
                            _class='form-group-seed'
                        ),
                        _class='form-group'
                    ),
                    Div(
                        Label('Guidance Scale (CFG):'),
                        Input(type='range', name='guidance_scale', min='0', max='2', step='0.1', value='1', 
                              oninput='updateGuidanceScale(this.value)'),
                        Span('1', id='guidanceScaleDisplay', style='margin-left: 10px;'),
                        _class='form-group'
                    ),
                    Div(
                        Label('Number of Images:'),
                        Input(type='number', name='num_images', min='1', max='4', value='1'),
                        _class='form-group'
                    ),
                    Div(
                        Label('Enable Safety Checker:'),
                        Input(type='checkbox', name='enable_safety_checker', checked=True),
                        _class='form-group'
                    ),
                    Button('Submit', type='submit', hx_post='/generate', hx_target='#result'),
                    _hx_boost=True,
                ),
                _class='form-container'
            ),
            Div(
                Div(id='result', _class='image-container'),
                _class='image-container'
            ),
            _class='main-container'
        )
    )

def render_error_page(message):
    return Div(P(message), id='result', _class='image-container')

def render_images(images):
    image_elements = [Img(src=image['url'], alt=f"Generated Image {i+1}", style="margin-bottom: 20px;") for i, image in enumerate(images)]
    return Div(
        *image_elements,
        id='result',
        _class='image-container'
    )
