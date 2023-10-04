
let ElementTargetValue = null;
let Select_Data_Gattering = document.querySelector("#Select_Data_Gattering");
let GatherDataInputConatiner = document.querySelector("#GatherDataInputConatiner");
Select_Data_Gattering.addEventListener("change",(element)=>{
    let AppendHtml = "";
    ElementTargetValue = element.target.value;
    console.log("This is an event select value:",ElementTargetValue);
    if(ElementTargetValue === "DatabaseConnection"){
        AppendHtml += `<div class="row">
            <div class="col-md-6"><label for="APIkey"> Database API Key </label></div>
            <div class="col-md-6"><input id="APIkey" type="text"></div>
            <div class="col-md-6"><label for="APIpassword"> Database API Key Password </label></div>
            <div class="col-md-6"><input id="APIpassword" type="text"></div>
            <div class="col-md-6"><label for="APISource"> Database API Source </label></div>
            <div class="col-md-6"><input id="APISource" type="text"></div>
        </div>`;
        GatherDataInputConatiner.innerHTML=AppendHtml;
    }else if(ElementTargetValue === "CSV"){
        AppendHtml += `<div class="row">
            <div class="col-md-12">
                <div id="drop-area">
                <h2> Drop files here or click to select files</h2>
                <input type="file" id="fileInput">
                </div>
            </div>
        </div>`;
        GatherDataInputConatiner.innerHTML=AppendHtml;
    }else if(ElementTargetValue === "ExcelFile"){
        AppendHtml += `<div class="row">
            <div class="col-md-12">
                <div id="drop-area">
                <h2> Drop files here or click to select files</h2>
                <input type="file" id="fileInput">
                </div>
            </div>
        </div>`;
        GatherDataInputConatiner.innerHTML=AppendHtml;
    }else if(ElementTargetValue === "JSON"){
        AppendHtml += `<div class="row">
            <div class="col-md-6"><label for="APIkey"> Add Json Path </label></div>
            <div class="col-md-6"><input id="APIkey" type="text"></div>
        </div>`;
        GatherDataInputConatiner.innerHTML=AppendHtml;
    }
    else{
        GatherDataInputConatiner.innerHTML=AppendHtml;
    }
})

