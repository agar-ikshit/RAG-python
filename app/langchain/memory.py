from langchain.memory import ConversationBufferMemory

# Memory per session/user (for simplicity, we use a dict to simulate sessions)
user_memories = {}

def get_memory(user_id: str):
    if user_id not in user_memories:
        user_memories[user_id] = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True,
            output_key="answer"
        )
    return user_memories[user_id]
