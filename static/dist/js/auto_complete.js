$(".autocomplete_search").autocomplete({
    minLength: 2,
    source:
        function (request, response) {
            $.getJSON(autocomplete_url, { term: request.term }, function (data) {
                response($.map(data, function (item) {
                    return {
                        label: item.name,
                        value: item.name,
                        id: item.id,
                    };
                }));
            });
        },
    change: function (event, ui) {
        window.location = "/product/" + ui.item.id;
    }
});

