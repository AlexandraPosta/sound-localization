// GET : to request data from the server.
// POST : to submit data to be processed to the server.

// Ready block.
$(document).ready(function() {
    console.log( "DOM ready!" );
    let self = this

    $('#room_apply').click(function( e ) {
        room_dim = [$('#room_l').val(), $('#room_w').val()]
        src = [$('#source_x').val(), $('#source_y').val()]
        mic = [[$('#mic_1_x').val(), $('#mic_1_y').val()],[$('#mic_2_x').val(), $('#mic_2_y').val()]]

        $.ajax({ 
            url: 'http://localhost:8000/endpoint?',
            type: 'GET',
            data: { 
                'type': 'getroom',
                'room': room_dim,
                'src': src,
                'mic': mic
            },
            error: function(errorThrown){
                console.log(errorThrown);
            },
            success: function(response){
                if (response) {
                    $('#results').empty().prepend(response);
                }
            }
        });
    });

    
    $('#run_model').click(function( e ) {
        model = $('#model_type').val()
        
        $.ajax({ 
            url: 'http://localhost:8000/endpoint?',
            type: 'GET',
            data: { 
                'type': 'run_model',
                'model': model
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

    $('#run_model').click(function( e ) {
        model = $('#model_type').val()
        
        $.ajax({ 
            url: 'http://localhost:8000/endpoint?',
            type: 'GET',
            data: { 
                'type': 'run_model',
                'model': model
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