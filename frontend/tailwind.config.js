module.exports = {
  future: {
    // removeDeprecatedGapUtilities: true,
    // purgeLayersByDefault: true,
  },
  purge: [
            "./public/**/*.html",
            './src/**/*.vue'
         ],
  theme: {
    extend: {},
    container: {
      padding: {
        default: '1rem',
        sm: '2rem',
        lg: '4rem',
        xl: '12rem',
      }
    }
  },
  // variants: {},
  plugins: [],
}
