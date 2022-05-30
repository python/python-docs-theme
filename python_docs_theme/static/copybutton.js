
const loadCopyButton = () => {
    /* Add a [>>>] button on the top-right corner of code samples to hide
     * the >>> and ... prompts and the output and thus make the code
     * copyable. */
    const hide_text = "Hide the prompts and output"
    const show_text = "Show the prompts and output"

    const button = document.createElement("span")
    button.classList.add("copybutton")
    button.innerText = ">>>"
    button.title = hide_text
    button.dataset.hidden = "false"
    const buttonClick = event => {
        // define the behavior of the button when it's clicked
        event.preventDefault()
        const buttonEl = event.currentTarget
        const codeEl = buttonEl.nextElementSibling
        if (buttonEl.dataset.hidden === "false") {
            // hide the code output
            codeEl.querySelectorAll('.go, .gp, .gt').forEach(el => el.hidden = true)
            codeEl.querySelectorAll('.gt').forEach(el => {
                while ((el = el.nextSibling) && el.nodeType !== Node.DOCUMENT_NODE) {
                    if (el.nodeType === Node.ELEMENT_NODE && el.matches(".gp, .go")) break;
                    if (el.nodeType === Node.TEXT_NODE && el.textContent.trim()) {
                        const wrapper = document.createElement('span');
                        el.after(wrapper);
                        wrapper.appendChild(el);
                        el = wrapper
                    }
                    el.hidden = true
                }
            })
            buttonEl.title = show_text
            buttonEl.dataset.hidden = "true"
        } else {
            // show the code output
            codeEl.childNodes.forEach(el => el.hidden = false)
            buttonEl.title = hide_text
            buttonEl.dataset.hidden = "false"
        }
    }

    const highlightedElements = document.querySelectorAll(
        ".highlight-python .highlight,"
        + ".highlight-python3 .highlight,"
        + ".highlight-pycon .highlight,"
        + ".highlight-pycon3 .highlight,"
        + ".highlight-default .highlight"
    )

    // create and add the button to all the code blocks that contain >>>
    highlightedElements.forEach(el => {
        el.style.position = "relative"

        // if we find a console prompt (.gp), prepend the (deeply cloned) button
        const clonedButton = button.cloneNode(true)
        // the onclick attribute is not cloned, set it on the new element
        clonedButton.onclick = buttonClick
        if (el.querySelector(".gp") !== null) {
            el.prepend(clonedButton)
        }
    })
}

if (document.readyState !== "loading") {
    loadCopyButton()
} else {
    document.addEventListener("DOMContentLoaded", loadCopyButton)
}
