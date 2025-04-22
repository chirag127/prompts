# prompts


cd ..
npx create-expo-app --template blank YTSummarizer11-react-native-expo-app
cd YTSummarizer11-react-native-expo-app
code .


npx create-expo-app --template blank qrsay-admin-frontend-react-native-expo-app
cd qrsay-admin-frontend-react-native-expo-app



npx expo export -p web
netlify deploy --prod --dir dist



cd frontend && npx create-expo-app . --template blank