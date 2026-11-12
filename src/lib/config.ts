export const siteConfig = {
  siteUrl: 'https://wrapped-2026-culture.true-cabin-9905.chatgpt.site',
  tokenName: 'Wrapped 2026',
  ticker: '$WRAPPED',
  network: 'Solana',
  contractAddress: '',
  xUrl: 'https://x.com/Wrappedonsol_',
  tradingUrl: '',
  dexScreenerUrl: '',
  launchStatus: 'Coming soon',
};
export function safeUrl(value: string): string | undefined {
  try { const url = new URL(value); return url.protocol === 'https:' ? url.href : undefined; } catch { return undefined; }
}
