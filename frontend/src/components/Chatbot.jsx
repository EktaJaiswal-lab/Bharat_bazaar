import { useState, useRef, useEffect } from 'react';
import { MessageSquare, X, Send, Bot, User } from 'lucide-react';
import { api } from '../config/api';

export default function Chatbot() {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([
    { role: 'model', content: "Hello! I'm the Bharat Bazaar AI Assistant. How can I help you discover the future of e-commerce today?" }
  ]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isOpen]);

  const handleSend = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage = input.trim();
    setInput('');
    
    // Format history for backend (exclude the very first greeting if needed, but it's fine to include)
    const history = messages.map(msg => ({
      role: msg.role,
      content: msg.content
    }));

    setMessages(prev => [...prev, { role: 'user', content: userMessage }]);
    setIsLoading(true);

    try {
      const response = await api.post('/chat/', {
        message: userMessage,
        history: history
      });
      
      setMessages(prev => [...prev, { role: 'model', content: response.data.reply }]);
    } catch (error) {
      console.error("Chat error:", error);
      setMessages(prev => [...prev, { role: 'model', content: "Sorry, I'm having trouble connecting to my neural network. Please try again." }]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <>
      {/* Floating Button */}
      <button 
        onClick={() => setIsOpen(!isOpen)}
        className={`fixed bottom-6 right-6 p-4 rounded-full shadow-[0_0_15px_rgba(102,252,241,0.5)] z-50 transition-all duration-300 hover:scale-110 ${isOpen ? 'bg-brand-gray text-white' : 'bg-brand-cyan text-brand-dark'}`}
      >
        {isOpen ? <X className="w-6 h-6" /> : <MessageSquare className="w-6 h-6" />}
      </button>

      {/* Chat Window */}
      <div 
        className={`fixed bottom-24 right-6 w-80 sm:w-96 h-[500px] max-h-[70vh] glass flex flex-col rounded-2xl overflow-hidden z-50 transition-all duration-300 origin-bottom-right ${isOpen ? 'scale-100 opacity-100' : 'scale-0 opacity-0 pointer-events-none'}`}
      >
        {/* Header */}
        <div className="bg-brand-gray/80 p-4 border-b border-white/10 flex items-center">
          <Bot className="w-6 h-6 text-brand-cyan mr-2" />
          <div>
            <h3 className="font-bold text-white leading-tight">AI Assistant</h3>
            <p className="text-xs text-brand-cyan">Online</p>
          </div>
        </div>

        {/* Messages */}
        <div className="flex-1 overflow-y-auto p-4 space-y-4">
          {messages.map((msg, idx) => (
            <div key={idx} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
              <div className={`max-w-[80%] rounded-2xl px-4 py-2 ${
                msg.role === 'user' 
                  ? 'bg-brand-purple text-white rounded-tr-sm' 
                  : 'bg-brand-gray/50 border border-white/10 text-gray-200 rounded-tl-sm'
              }`}>
                <p className="text-sm whitespace-pre-wrap">{msg.content}</p>
              </div>
            </div>
          ))}
          {isLoading && (
            <div className="flex justify-start">
              <div className="bg-brand-gray/50 border border-white/10 rounded-2xl rounded-tl-sm px-4 py-3 flex space-x-2">
                <div className="w-2 h-2 bg-brand-cyan rounded-full animate-bounce"></div>
                <div className="w-2 h-2 bg-brand-cyan rounded-full animate-bounce" style={{ animationDelay: '0.2s' }}></div>
                <div className="w-2 h-2 bg-brand-cyan rounded-full animate-bounce" style={{ animationDelay: '0.4s' }}></div>
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        {/* Input */}
        <div className="p-4 bg-brand-gray/80 border-t border-white/10">
          <form onSubmit={handleSend} className="relative">
            <input 
              type="text" 
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Ask me anything..." 
              className="w-full bg-brand-dark border border-gray-600 rounded-full py-3 pl-4 pr-12 text-sm text-white focus:outline-none focus:border-brand-cyan focus:ring-1 focus:ring-brand-cyan"
              disabled={isLoading}
            />
            <button 
              type="submit" 
              disabled={!input.trim() || isLoading}
              className="absolute right-2 top-2 p-1.5 rounded-full bg-brand-cyan text-brand-dark disabled:opacity-50 disabled:cursor-not-allowed hover:bg-white transition-colors"
            >
              <Send className="w-4 h-4" />
            </button>
          </form>
        </div>
      </div>
    </>
  );
}
