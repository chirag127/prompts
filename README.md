# prompts


cd ..
npx create-expo-app --template blank YTSummarizer11-react-native-expo-app
cd YTSummarizer11-react-native-expo-app
code .

cd ..
npx create-expo-app --template blank all-pdf-tools6
cd all-pdf-tools6
code .


npx create-expo-app --template blank qrsay-user-frontend-react-native-expo-app
cd qrsay-user-frontend-react-native-expo-app

npx create-expo-app --template blank pdf-tools6
cd pdf-tools6

npx expo export -p web
netlify deploy --prod --dir dist



cd frontend && npx create-expo-app . --template blank