'use client';

import { useState } from 'react';
import ChatInterface from '@/components/ChatInterface';
import Header from '@/components/Header';

export default function HomePage() {
  const [isChatOpen, setIsChatOpen] = useState(false);

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <Header />
      
      <main className="max-w-4xl mx-auto px-4 py-12">
        {!isChatOpen ? (
          <div className="text-center">
            <h1 className="text-5xl font-bold text-gray-900 mb-6">
              Welcome to <span className="text-primary-600">Zlodowy</span>
            </h1>
            <p className="text-xl text-gray-600 mb-8 max-w-2xl mx-auto">
              Experience the power of AI with our advanced chat interface powered by OpenAI GPT-4. 
              Start a conversation and discover what's possible.
            </p>
            
            <div className="space-y-4">
              <button
                onClick={() => setIsChatOpen(true)}
                className="btn-primary text-lg px-8 py-3"
                aria-label="Start chatting with AI"
              >
                Start Chatting
              </button>
              
              <div className="flex justify-center space-x-4 text-sm text-gray-500">
                <span>✨ Powered by GPT-4</span>
                <span>🚀 Built with Next.js & FastAPI</span>
                <span>⚡ Real-time responses</span>
              </div>
            </div>
          </div>
        ) : (
          <ChatInterface onClose={() => setIsChatOpen(false)} />
        )}
      </main>
    </div>
  );
} 