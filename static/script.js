async function correctText(){

    const text =
    document.getElementById("inputText").value;

    if(text.trim() === ""){
        alert("Please enter some text");
        return;
    }

    const response = await fetch('/correct',{

        method:'POST',

        headers:{
            'Content-Type':'application/json'
        },

        body:JSON.stringify({
            text:text
        })

    });

    const data = await response.json();

    const originalWords =
    data.original.split(" ");

    const correctedWords =
    data.corrected.split(" ");

    let result = "";

    for(let i=0;i<correctedWords.length;i++){

        if(originalWords[i] !== correctedWords[i]){

            result +=
            `<span class="changed">${correctedWords[i]}</span> `;

        }else{

            result += correctedWords[i] + " ";

        }
    }

    document.getElementById("output").innerHTML =
    result;

    document.getElementById("count").innerText =
    data.changes;
}