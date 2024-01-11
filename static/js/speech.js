const audio = document.getElementById("audio_track");
const audio_spinner = document.getElementById("speech_loader");
const audio_form = document.querySelector('form[name="get_text"]')
audio_form.addEventListener("submit", async evt => {
        evt.preventDefault()
        audio_spinner.classList.remove("d-none")
        audio.classList.add("d-none")
        await fetch("/upload-text", {
            method: "post",
            body: new FormData(evt.target)

        }).then(response => response.json()).then(data => {
            // const audioUrl = "/home/ashkaneskandari/mysite/UPLOADS/audio/audio_path.mp3";
            const audioUrl = data.audio_url;
            document.getElementById("oggSource").src = audioUrl;
            document.getElementById("mp3Source").src = audioUrl;
            audio.load();
            audio_spinner.classList.add("d-none")
            audio.classList.remove("d-none")
            audio.play();
        })

    })