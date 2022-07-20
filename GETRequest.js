import { WebClient } from 'https://deno.land/x/slack_web_api/mod.js';

// const { WebClient } = require('@slack/web-api');
 const token = process.env.BOT_TOKEN;
 const client = new WebClient(token);

// // Store conversation history
let conversationHistory;
// // ID of channel you watch to fetch the history for
let channelId = "C03QTRM7XJ4";

try {
  //   // Call the conversations.history method using WebClient
  const result = client.conversations.history({
    channel: channelId
  });

  conversationHistory = result.messages;

  //   // Print results
  console.log(conversationHistory.length + " messages found in " + channelId);
}
catch (error) {
  console.error(error);
}