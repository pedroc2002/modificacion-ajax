$(function(){
    let objectNumberArray = 0;
    let data = [];
    const button = $("#btn");
    const elementTitle = $("#title");
    const elementContent = $("#content");
    const elementInfram = $("#video");

    function paintElements() {
        const objectData = data[objectNumberArray];
        elementTitle.html(objectData.title);
        elementContent.html(objectData.content);
        elementInfram.attr("src", objectData.url);
    }
    
    function getData(){
        return $.ajax("ajax.json", {
            type: "GET",
        });
    };

    function changeVideo(){
        button.on("click", function(){
            if (data.length == 0) {
                getData().then((responseData) =>{
                    data = responseData;
                    paintElements();
                    objectNumberArray++;
                });
            }
            else{
                paintElements();
                objectNumberArray == 2 ? objectNumberArray = 0: objectNumberArray++;
            }
        });
    }
    changeVideo();
});