import { Link, Outlet, createFileRoute } from "@tanstack/react-router";

import { Nav } from "@/components/Layout/Client/Nav";

const footerNavItems = [
  { to: "/", label: "Home" },
  { to: "/news", label: "News" },
  { to: "/blog", label: "Blog" },
  { to: "/about", label: "About" },
] as const;

const socialItems = [
  { href: "https://github.com/yyong008/fastapi-antd-admin", label: "GitHub" },
  { href: "https://x.com", label: "X/Twitter" },
  { href: "mailto:contact@example.com", label: "Email" },
] as const;

export const Route = createFileRoute("/_client")({
  component: ClientNav,
});

function ClientNav() {
  return (
    <div className="relative flex min-h-screen flex-col bg-slate-50">
      <Nav />
      <main className="mx-auto w-full max-w-7xl flex-1 px-6 pt-24 lg:px-10">
        <Outlet />
      </main>
      <footer className="mt-12 w-full border-t border-slate-200 bg-white/90 backdrop-blur">
        <div className="mx-auto w-full max-w-7xl px-6 py-10 lg:px-10">
          <div className="flex flex-col items-start justify-between gap-6 md:flex-row md:items-center">
            <div>
              <p className="text-base font-semibold text-slate-900">FastAPI Admin</p>
              <p className="mt-2 text-sm text-slate-500">Build and ship your admin system faster.</p>
            </div>
            <div className="flex flex-wrap items-center gap-2">
              {footerNavItems.map((item) => (
                <Link
                  key={item.to}
                  className="rounded-md px-3 py-2 text-sm text-slate-600 transition-colors hover:bg-slate-100 hover:text-slate-900"
                  to={item.to}
                >
                  {item.label}
                </Link>
              ))}
            </div>
            <div className="flex items-center gap-2">
              {socialItems.map((item) => (
                <a
                  key={item.label}
                  className="rounded-md px-3 py-2 text-sm text-slate-600 transition-colors hover:bg-slate-100 hover:text-slate-900"
                  href={item.href}
                  target={item.href.startsWith("mailto:") ? undefined : "_blank"}
                  rel={item.href.startsWith("mailto:") ? undefined : "noreferrer"}
                >
                  {item.label}
                </a>
              ))}
            </div>
          </div>
          <div className="mt-8 border-t border-slate-200 pt-6 text-xs text-slate-500">
            {new Date().getFullYear()} FastAPI Antd Admin. All rights reserved.
          </div>
        </div>
      </footer>
    </div>
  );
}
