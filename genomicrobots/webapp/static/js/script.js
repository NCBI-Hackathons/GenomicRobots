$(function() {
      // console.log("ping");
      $('[data-toggle="popover"]').popover({
          trigger: 'hover',
              'placement': 'top'
      });

      $.ajaxSetup({
            headers: { 'X-CSRFToken': _csrf_token}
      });

});