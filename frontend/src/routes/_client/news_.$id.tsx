import { NewsContent } from "@/components/Client/NewsDetail/news-content";
import { NewsHeader } from "@/components/Client/NewsDetail/news-header";
import { createFileRoute } from "@tanstack/react-router";
import { getNewsById } from "@/apis/client/news";

export const Route = createFileRoute("/_client/news_/$id")({
  component: NewsDetailRoute,
  async loader({ params }) {
    const result: any = await getNewsById(Number(params.id));
    if (result && result.code === 0) {
      return result.data;
    }
  },
});

export function NewsDetailRoute() {
  const news = Route.useLoaderData();
  return (
    <section className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
      <div className="font-sans text-base/loose">
        <NewsHeader news={news} />
        <NewsContent content={news.content} />
      </div>
    </section>
  );
}
