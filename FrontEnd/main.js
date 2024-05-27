textInput = document.getElementById('text')
resultOutput = document.getElementById('result')

const goClickHandler = () => {
    console.log(textInput.value);
    const data = JSON.stringify({
        text: textInput.value
    });
    
    fetch('http://127.0.0.1:8000/',{
        method: "POST",
        mode: "cors",
        headers: {
            "Content-Type": "application/json"
        },
        body: data
    })
    .then((response) => response.json())
    .then((json) => {
        console.log(json);
        resultOutput.innerHTML = json['prediction']
    });
}