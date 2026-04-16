import { Link } from "@tanstack/react-router";

import { HeaderLink } from "./HeaderLink";

const mainNavItems = [
  { to: "/", label: "Home" },
  { to: "/news", label: "News" },
  { to: "/blog", label: "Blog" },
  { to: "/about", label: "About" },
] as const;

const actionNavItems = [{ to: "/login", label: "Login" }] as const;

export function Nav() {
  return (
    <header className="fixed inset-x-0 top-0 z-50 border-b border-slate-200/60 bg-white/90 backdrop-blur">
      <div className="mx-auto flex h-16 w-full max-w-7xl items-center justify-between px-6 lg:px-10">
        <div className="flex items-center gap-8">
          <Link
            className="inline-flex items-center rounded-md px-3 py-2 text-sm font-semibold text-slate-900 transition-colors duration-200 hover:bg-slate-100"
            to="/"
          >
            FastAPI Admin
          </Link>
          <nav className="flex items-center gap-1">
            {mainNavItems.map((item) => (
              <HeaderLink key={item.to} to={item.to}>
                {item.label}
              </HeaderLink>
            ))}
          </nav>
        </div>
        <div className="flex items-center gap-2">
          {actionNavItems.map((item) => (
            <HeaderLink key={item.to} to={item.to} variant="button">
              {item.label}
            </HeaderLink>
          ))}
        </div>
      </div>
    </header>
  );
}
