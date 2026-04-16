import { createFileRoute } from "@tanstack/react-router";
export const Route = createFileRoute("/_client/")({
  component: Home,
});

function Home() {
  return (
    <section className="relative overflow-hidden rounded-2xl border border-slate-200 bg-white">
      <div className="absolute inset-0 bg-gradient-to-br from-slate-50 via-white to-indigo-50" />
      <div className="relative mx-auto flex min-h-[60vh] max-w-3xl flex-col items-center justify-center px-6 py-16 text-center">
        <p className="mb-4 rounded-full border border-slate-200 bg-white px-4 py-1 text-sm text-slate-600">
          Commercial Ready Starter
        </p>
        <h1 className="mb-4 text-4xl font-semibold tracking-tight text-slate-900 md:text-5xl">
          FastAPI Antd Admin
        </h1>
        <p className="mb-8 text-base leading-7 text-slate-600 md:text-lg">
          A lightweight content management system, not limited to content management.
        </p>
        <a
          className="inline-flex items-center rounded-md bg-slate-900 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-slate-700"
          href="https://github.com/yyong008/fastapi-antd-admin"
          target="_blank"
          rel="noreferrer"
        >
          View on GitHub
        </a>
      </div>
    </section>
  );
}
