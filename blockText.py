class Suggestions:


    def __init__(self,channel_id,user_id,jsonList):
        self.channel_id = channel_id
        self.user = user_id
        self.timestamp = ''
        self.lists = jsonList
        if len(self.lists) ==4:
            self.START_TEXT = [{
                    'type': 'section',
                    'text': {
                        'type': 'plain_text',
                        'text': 'Here is a list of valuable suggestions\n Hover and click on link to see if your question has already been answered in this channel',
                        }
                },
                {
                    "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": self.lists[0]["resultLink"]
                        },
                        "accessory": {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Helpful?"
                            },
                            "style": "primary",
                            "value": self.lists[0]["resultLink"],
                            "action_id": "button"
                        }
                },
                {
                    "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": self.lists[1]["resultLink"]
                        },
                        "accessory": {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Helpful?"
                            },
                            "style": "primary",
                            "value": self.lists[1]["resultLink"],
                            "action_id": "button"
                        }
                },
                {
                    "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": self.lists[2]["resultLink"]
                        },
                        "accessory": {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Helpful?"
                            },
                            "style": "primary",
                            "value": self.lists[2]["resultLink"],
                            "action_id": "button"
                        }
                },
                {
                    "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": self.lists[3]["resultLink"]
                        },
                        "accessory": {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Helpful?"
                            },
                            "style": "primary",
                            "value": self.lists[3]["resultLink"],
                            "action_id": "button"
                        }
                },
                {
			        "type": "actions",
			        "block_id": "actionblock789",
			        "elements": [
				        {
					    "type": "button",
					    "text": {
						        "type": "plain_text",
						        "text": "Not Helpful"
					    },
					        "style": "danger",
					        "value": "click_me_456"
				    }
                    ]
                }]
        if len(self.lists) == 3:
            self.START_TEXT = [{
                    'type': 'section',
                    'text': {
                        'type': 'plain_text',
                        'text': 'Here is a list of valuable suggestions\n Hover and click on link to see if your question has already been answered',
                        }
                },
                {
                    "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": self.lists[0]["resultLink"]
                        },
                        "accessory": {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Helpful?"
                            },
                            "style": "primary",
                            "value": self.lists[0]["resultLink"],
                            "action_id": "button"
                        }
                },
                {
                    "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": self.lists[1]["resultLink"]
                        },
                        "accessory": {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Helpful?"
                            },
                            "style": "primary",
                            "value": self.lists[1]["resultLink"],
                            "action_id": "button"
                        }
                },
                {
                    "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": self.lists[2]["resultLink"]
                        },
                        "accessory": {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Helpful?"
                            },
                            "style": "primary",
                            "value": self.lists[2]["resultLink"],
                            "action_id": "button"
                        }
                },
                {
			        "type": "actions",
			        "block_id": "actionblock789",
			        "elements": [
				        {
					    "type": "button",
					    "text": {
						        "type": "plain_text",
						        "text": "Not Helpful"
					    },
					        "style": "danger",
					        "value": "click_me_456"
				    }
                    ]
                }]
        if len(self.lists) == 2:
            self.START_TEXT = [{
                    'type': 'section',
                    'text': {
                        'type': 'plain_text',
                        'text': 'Here is a list of valuable suggestions\n Hover and click on link to see if your question has already been answered',
                        }
                },
                {
                    "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": self.lists[0]["resultLink"]
                        },
                        "accessory": {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Helpful?"
                            },
                            "style": "primary",
                            "value": self.lists[0]["resultLink"],
                            "action_id": "button"
                        }
                },
                {
                    "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": self.lists[1]["resultLink"]
                        },
                        "accessory": {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Helpful?"
                            },
                            "style": "primary",
                            "value": self.lists[1]["resultLink"],
                            "action_id": "button"
                        }
                },
                {
			        "type": "actions",
			        "block_id": "actionblock789",
			        "elements": [
				        {
					    "type": "button",
					    "text": {
						        "type": "plain_text",
						        "text": "Not Helpful"
					    },
					        "style": "danger",
					        "value": "click_me_456"
				    }
                    ]
                }]
        if len(self.lists) == 1:
            self.START_TEXT = [{
                    'type': 'section',
                    'text': {
                        'type': 'plain_text',
                        'text': 'Here is a list of valuable suggestions\n Hover and click on link to see if your question has already been answered',
                        }
                },
                {
                    "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": self.lists[0]["resultLink"]
                        },
                        "accessory": {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Helpful?"
                            },
                            "style": "primary",
                            "value": self.lists[0]["resultLink"],
                            "action_id": "button"
                        }
                },
                {
			        "type": "actions",
			        "block_id": "actionblock789",
			        "elements": [
				        {
					    "type": "button",
					    "text": {
						        "type": "plain_text",
						        "text": "Not Helpful"
					    },
					        "style": "danger",
					        "value": "click_me_456"
				    }
                    ]
                }]
            
    def getmessage(self):
        return {
            'channel':self.channel_id,
            'user':self.user,
            'blocks': self.START_TEXT
            
        }