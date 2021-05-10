let currentTheme = localStorage.getItem('currentTheme') || 'auto'

const pygmentsDark = document.getElementById('pygments_dark_css')
const pydocthemeDark = document.getElementById('pydoctheme_dark_css')

const themeOrder = {
  light: 'dark',
  dark: 'auto',
  auto: 'light',
}

updateTheme()

function toggleTheme() {
  currentTheme = themeOrder[currentTheme]
  localStorage.setItem('currentTheme', currentTheme)
  updateTheme()
}

function updateTheme() {
  const buttons = Array.from(document.getElementsByClassName('theme-toggle'))
  switch (currentTheme) {
    case 'light':
      pydocthemeDark.media = 'not all'
      pygmentsDark.media = 'not all'
      buttons.forEach(e => e.value = "Toggle theme (light)")
      break;
    case 'dark':
      pydocthemeDark.media = 'all'
      pygmentsDark.media = 'all'
      buttons.forEach(e => e.value = "Toggle theme (dark)")
      break;
    default:
      // auto
      pydocthemeDark.media = '(prefers-color-scheme: dark)'
      pygmentsDark.media = '(prefers-color-scheme: dark)'
      buttons.forEach(e => e.value = "Toggle theme (auto)")
  }
}
