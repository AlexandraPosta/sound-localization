// GET : to request data from the server.
// POST : to submit data to be processed to the server.

// Ready block.
$(document).ready(function() {
    console.log( "DOM ready!" );

    $('button').click(function( e ) {
        room_dimensions = []
        source = []
        microphone = []

        $.ajax({ 
            url: 'http://localhost:8000/endpoint?',
            type: 'GET',
            data: { 
                'type': 'getroom',
                'room': 'test',
                'source': 'test',
                'microphone': 'test'
            },
            error: function(errorThrown){
                console.log(errorThrown);
            },
            success: function(response){
                if (response) {
                    $('#results').prepend(response);
                }
            }
        });
    });
});