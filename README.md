# prompts


cd ..
npx create-expo-app --template blank YTSummarizer7-react-native-expo-app
cd YTSummarizer7-react-native-expo-app
code .






npx expo export -p web
netlify deploy --prod --dir dist



cd frontend && npx create-expo-app . --template blank