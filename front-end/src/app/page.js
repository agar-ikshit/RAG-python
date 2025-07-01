"use client";

import { useState, useRef, useEffect } from "react";
import { marked } from "marked";
import DOMPurify from "dompurify";
import Sidebar from "./components/Sidebar";

export default function Home() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [isSidebarOpen, setIsSidebarOpen] = useState(false); // Add state for sidebar toggle
  const chatBoxRef = useRef(null);
  const userCounterRef = useRef(1);

  useEffect(() => {
    if (chatBoxRef.current) {
      chatBoxRef.current.scrollTop = chatBoxRef.current.scrollHeight;
    }
  }, [messages]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    setMessages((prev) => [...prev, { sender: "You", text: input, side: "right" }]);
    setInput("");
    setIsLoading(true);

    const tempMessage = { sender: "Bot", text: "Typing...", side: "left" };
    setMessages((prev) => [...prev, tempMessage]);

    const userId = `test-user-${userCounterRef.current++}`;

    try {
      const res = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_id: userId, question: input }),
      });

      if (!res.ok) {
        throw new Error("Network response was not ok");
      }

      const data = await res.json();
      const botAnswer = data.answer || "No response.";
      const parsedAnswer = DOMPurify.sanitize(marked.parse(botAnswer, { async: false }));

      setMessages((prev) =>
        prev.map((msg, index) =>
          index === prev.length - 1 ? { sender: "Bot", text: parsedAnswer, side: "left" } : msg
        )
      );
    } catch (err) {
      console.error("Error:", err);
      setMessages((prev) =>
        prev.map((msg, index) =>
          index === prev.length - 1
            ? { sender: "Bot", text: "Sorry, something went wrong.", side: "left" }
            : msg
        )
      );
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex min-h-screen">
      {/* Sidebar (Conditional) */}
      <div className={`md:block ${isSidebarOpen ? "block" : "hidden"}`}>
        <Sidebar />
      </div>

      {/* Main Chatbot Area */}
      <div className={`flex-1 flex justify-end items-end p-1 ${isSidebarOpen ? "ml-64 md:ml-64" : "ml-0"}`}>
        {/* Toggle Button for Mobile */}
        <button
          className="md:hidden p-2 bg-[#EE3953] text-white rounded mb-4"
          onClick={() => setIsSidebarOpen(!isSidebarOpen)}
        >
          {isSidebarOpen ? "Close Sidebar" : "Open Sidebar"}
        </button>

        <div className="bg-white shadow-xl rounded-lg w-full max-w-5xl p-6">
          <h2 className="text-2xl font-semibold mb-4 text-center text-[#EE3953]">
            Logicspice Product Chatbot
          </h2>

          <div
            ref={chatBoxRef}
            className="flex flex-col gap-3 mb-4 h-[75vh] overflow-y-auto border border-gray-200 rounded p-4 bg-gray-50 scroll-smooth"
          >
            {messages.map((msg, index) => (
              <div
                key={index}
                className={`text-sm p-2 rounded max-w-lg whitespace-pre-wrap ${
                  msg.side === "right"
                    ? "bg-blue-100 self-end text-right ml-auto"
                    : "bg-gray-200 self-start"
                }`}
              >
                {msg.text === "Typing..." ? (
                  <div className="flex items-center gap-2">
                    <strong>Bot:</strong>
                    <div className="animate-spin h-5 w-5 border-2 border-[#EE3953] border-t-transparent rounded-full"></div>
                  </div>
                ) : (
                  <div
                    dangerouslySetInnerHTML={{
                      __html: `<strong>${msg.sender}:</strong> ${msg.text}`,
                    }}
                  />
                )}
              </div>
            ))}
          </div>

          <form onSubmit={handleSubmit} className="flex gap-2">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Ask about Logicspice products..."
              className="flex-grow p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-[#EE3953]"
              disabled={isLoading}
              required
            />
            <button
              type="submit"
              disabled={isLoading}
              className="bg-[#EE3953] text-white px-4 py-2 rounded disabled:opacity-50"
            >
              Ask
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}