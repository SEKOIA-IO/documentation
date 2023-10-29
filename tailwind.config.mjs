/** @type {import('tailwindcss').Config} */
const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
	content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
	theme: {
		extend: {
			fontFamily: {
				sans: ['Inter var', ...defaultTheme.fontFamily.sans],
			},
			colors: {
				brand: {
					50: '#EEEBFC',
					100: '#E0DCFE',
					200: '#E0DCFE',
					300: '#C1B9FD',
					400: '#A095FB',
					500: '#5D4FF2',
					600: '#4539D0',
					700: '#3027AE',
					800: '#1F198C',
					900: '#140F74',
					yellow: '#EDC627',
					white: '#F5F5FA',
				},
			}
		},
	},
	plugins: [
		require('@tailwindcss/forms'),
		require('@tailwindcss/typography'),
	],
}
