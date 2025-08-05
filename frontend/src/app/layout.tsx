import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'Zlodowy - AI Chat Application',
  description: 'A modern full-stack AI chat application with OpenAI GPT-4 integration',
  keywords: ['AI', 'Chat', 'OpenAI', 'GPT-4', 'Next.js', 'FastAPI'],
  authors: [{ name: 'Zlodowy Team' }],
  viewport: 'width=device-width, initial-scale=1',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-gray-50">
        <div className="container mx-auto px-4 py-8">
          {children}
        </div>
      </body>
    </html>
  );
} 