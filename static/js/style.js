           $("#institution").on('change', () => {
                const institution = $("#institution").val().toLowerCase()
                fetch(`year-of-oldest-record/${institution}`).then(res => {
                    return res.json()
                }).then(
                    res => {
                        console.log(res)
                        $("#institution-name").text(res[0]['institution'])
                        $("#institution-oldest-record").text(res[1]['year_of_oldest_record'])
                        $("#institution-student-count").text(res[2]['number_of_students'])

                    }
                )
            })

