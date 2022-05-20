$(".autocomplete_search").autocomplete({
    minLength: 2,
    source:
        function (request, response) {
            const specialChars = `\`!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~`;
            $.getJSON(autocomplete_url, { term: request.term }, function (data) {
                response($.map(data, function (item) {
                    if (containsSpecialChars(item.name))
                        return {
                            label: item.name,
                            value: item.name.replace(specialChars),

                            id: item.id,
                        };
                    else {
                        return {
                            label: item.name,
                            value: item.name,
                            id: item.id,
                        }
                    }
                }));
            });
        },
    change: function (event, ui) {
        window.location = "/product/" + ui.item.id;
    }
});

function containsSpecialChars(str) {
    const specialChars = `\`!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~`;

    return specialChars.split('').some(specialChar => {
        return !!str.includes(specialChar);


    });
}
