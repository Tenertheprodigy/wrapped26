import type { Metadata } from 'next';
import './globals.css';
import { siteConfig } from '@/lib/config';
export const metadata: Metadata = {
  metadataBase: new URL(siteConfig.siteUrl),
  title: 'Wrapped 2026 | Music, Memories & Community on Solana',
  description: 'Celebrate the culture of Spotify Wrapped 2026 with an independent, community-powered Solana token. Explore the history, music, and moments that brought the internet together.',
  openGraph: { title: 'Wrapped 2026 — Your year. Your music. Our culture.', description: 'An independent celebration of music, memories, and community on Solana.', images: [{ url: '/social-preview.png', width: 1200, height: 630 }] },
  twitter: { card: 'summary_large_image', images: ['/social-preview.png'] },
};
export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="en"><body>{children}</body></html>;
}
