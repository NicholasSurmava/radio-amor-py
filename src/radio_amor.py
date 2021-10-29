from flask import (
    Blueprint, jsonify, current_app
)

amor = Blueprint('amor', __name__)

# NOTE: User needs to be logged into a premium spotify account to play the playlists within the app. Auth should redirect them to spotify to login then send them back here.
# NOTE: Add the ability for the user to save the playlist to their account from within the app? Need to check if possible.


@amor.route('/')
def index():
    # TODO: Return a list of RADIO AMOR playlists from my spotify
    # NOTE: Playlists should be marked as public and be in the radio amor folder
    current_app.logger.info('Amor index route')
    return 'hello\n'

# TODO: Add pages for each playlist. This will show a "fullscreen" view of a playlist with song selection.
